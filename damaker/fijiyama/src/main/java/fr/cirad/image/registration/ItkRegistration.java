package fr.cirad.image.registration;

import java.util.ArrayList;

import org.itk.simple.AffineTransform;
import org.itk.simple.CenteredTransformInitializerFilter;
import org.itk.simple.Command;
import org.itk.simple.Euler2DTransform;
import org.itk.simple.Euler3DTransform;
import org.itk.simple.EventEnum;
import org.itk.simple.Image;
import org.itk.simple.ImageRegistrationMethod;
import org.itk.simple.ResampleImageFilter;
import org.itk.simple.Similarity3DTransform;
import org.itk.simple.TranslationTransform;
import org.itk.simple.VectorDouble;
import org.itk.simple.VectorUInt32;
import org.itk.simple.VersorRigid3DTransform;

import fr.cirad.image.registration.CenteringStrategy;
import fr.cirad.image.registration.IterationUpdate;
import fr.cirad.image.registration.ItkRegistration;
import fr.cirad.image.registration.ItkTransform;
import fr.cirad.image.registration.MetricType;
import fr.cirad.image.registration.OptimizerType;
import fr.cirad.image.registration.SamplingStrategy;
import fr.cirad.image.registration.ScalerType;
import fr.cirad.image.registration.Transform3DType;

import fr.cirad.image.common.ItkImagePlusInterface;
import fr.cirad.image.common.VitiDialogs;
import fr.cirad.image.common.VitimageUtils;

import org.itk.simple.RecursiveGaussianImageFilter;

import ij.IJ;
import ij.ImagePlus;

public class ItkRegistration implements ItkImagePlusInterface{
	ItkTransform additionalTransform=new ItkTransform();
	public boolean returnComposedTransformationIncludingTheInitialTransformationGiven=true;
	public double[]refRange;
	public double[]movRange;
	public boolean flagRange=false;
	boolean lookLikeOptimizerLooks=false;
	boolean textInfoAtEachIteration=false;
	boolean movie3D=false;
	public int displayRegistration=1;
	CenteredTransformInitializerFilter centerTransformFilter;
	private RecursiveGaussianImageFilter gaussFilter;
	private ResampleImageFilter resampler;
	private double[]voxelSizeReference;
	private int[]imageSizeReference;
	private Image itkImgViewRef;
	private Image itkImgViewMov;
	private Image itkSummaryRef;
	private Image itkSummaryMov;
	private ImagePlus sliceViewMov;
	private ImagePlus sliceViewRef;
	private ImagePlus sliceView;
	private ImagePlus sliceSummaryRef;
	private ImagePlus sliceSummaryMov;
	//private ImagePlus summary;
	private ArrayList<ImagePlus> imgMovSuccessiveResults;
	private int viewWidth;
	private int viewHeight;
	private int viewSlice;
	private int zoomFactor;
	private IterationUpdate updater;
	private ArrayList<Integer> nbLevels;
	private ArrayList<int[]> shrinkFactors;
	private ArrayList<int[][]> dimensions;
	private ArrayList<double[]> sigmaFactors;
	private int currentLevel;
	private int basis=2;//shrink factor at each level

	private ArrayList<CenteringStrategy> centeringStrategies;
	private ArrayList<Transform3DType> transformation3DTypes;
	private ArrayList<ScalerType>scalerTypes;
	private int nbStep;
	private int currentStep;
	private MetricType metricType;
	private ArrayList<ImageRegistrationMethod> registrationMethods;
	public ImagePlus ijImgRef;
	private Image itkImgRef;
	private ImagePlus ijImgMov;
	private Image itkImgMov;
	private ArrayList<ImagePlus> registrationSummary;
	private ItkTransform transform;
	private ArrayList<double[]> weights;
	private ArrayList<double[]> scales;
	private int fontSize=12;
	public Thread registrationThread;
	public volatile boolean itkRegistrationInterrupted=false;
	public volatile boolean itkIsInterruptedSucceeded=false;

	public void freeMemory(){
		if(registrationSummary.size()>0) {
			registrationSummary=null;
		}
		itkImgMov=null;
		ijImgMov=null;
		itkImgRef=null;
		ijImgRef=null;

		itkImgViewRef=null;
		itkImgViewMov=null;
		itkSummaryRef=null;
		itkSummaryMov=null;
		sliceViewMov=null;
		sliceViewRef=null;
		sliceView=null;
		sliceSummaryRef=null;
		sliceSummaryMov=null;
		if(imgMovSuccessiveResults.size()>0) {
			imgMovSuccessiveResults=null;
		}
		System.gc();
	}
	
	/** 
	 * Top level functions : Test function, and main scenarios that will be used by customers classes
	 */
	public int runTestSequence() {
		
		//MATTES256 SUR VERSOR 2 3 PUIS SIMILITUDE 1 2 , avec AMOEBA et sigma 0.8 , 30  0.5 --> de la tuerie
		int nbFailed=0;
		ItkRegistration manager=new ItkRegistration();
		ImagePlus []imgTab=VitiDialogs.chooseTwoImagesUI("Choose reference image and moving image to register\n\n","Reference image","Moving image");
		manager.movie3D=VitiDialogs.getYesNoUI("Compute 3D summary ?","");
		ImagePlus imgRef=imgTab[0];
		ImagePlus imgMov=imgTab[1];
		manager.setMovingImage(imgMov);
		manager.setReferenceImage(imgRef);
		manager.setViewSlice(20);
		manager.setMetric(MetricType.MATTES);
		OptimizerType opt=OptimizerType.ITK_AMOEBA ;
		SamplingStrategy samplStrat=SamplingStrategy.NONE;
	/*	addStepToQueue( 30 20
				int levelMin,int levelMax,double sigma,Transform3DType typeTransfo,double[]weights,
				OptimizerType optimizerType,ScalerType scalerType,double[]scales, 
				boolean doubleIterAtCoarsestLevels,CenteringStrategy centeringStrategy,SamplingStrategy samplingStrategy
				);*/
		manager.addStepToQueue( 1 ,     4     ,     1     ,    2*2  , 0.8   ,       Transform3DType.VERSOR,    null,
						opt  , ScalerType.SCALER_PHYSICAL, null ,
				false,         CenteringStrategy.MASS_CENTER,    samplStrat  );
		
		manager.addStepToQueue( 1 ,    2     ,     0.8     ,   3*2,  0.8,     Transform3DType.SIMILARITY,    null,
				opt  , ScalerType.SCALER_PHYSICAL, null ,
				false,         CenteringStrategy.NONE,    samplStrat  );

		
		manager.register();
		freeMemory();
		return nbFailed;
	}
	
	public ItkTransform runScenarioFromGui(ItkTransform transformInit, ImagePlus imgRef, ImagePlus imgMov, Transform3DType transformType,int levelMin,int levelMax,int nIterations,double learningRate) {
		this.setMovingImage(imgMov);
		this.setReferenceImage(imgRef);
		this.setViewSlice(imgRef.getStackSize()/2);
		this.setMetric(MetricType.CORRELATION);
		OptimizerType opt=OptimizerType.ITK_AMOEBA ;
		SamplingStrategy samplStrat=SamplingStrategy.NONE;
		
		this.addStepToQueue( levelMin,     levelMax    ,     1     ,   nIterations  , learningRate   ,       transformType,    null,
				opt  , ScalerType.NONE/*ScalerType.SCALER_PHYSICAL*/, null ,
		false,         CenteringStrategy.IMAGE_CENTER,    samplStrat  );

		this.transform=ItkTransform.itkTransformFromCoefs(new double[] {1,0,0,0,0,1,0,0,0,0,1,0});//new ItkTransform(transformInit);
		this.register();
		if(this.itkRegistrationInterrupted)return null;
		if(this.returnComposedTransformationIncludingTheInitialTransformationGiven) return this.transform;
		else {
			if(transformInit.isDense())return new ItkTransform((transformInit.getInverseOfDenseField()).addTransform(this.transform));
			else return new ItkTransform(transformInit.getInverse().addTransform(this.transform));
		}
	}

	public static int estimateRegistrationDuration(int[]dims,int viewRegistrationLevel,int nbIter,int levelMin,int levelMax) {
		double imageSize=dims[0]*dims[1]*dims[2];
		double[]imageSizes=new double[levelMax-levelMin+1];
		double sumSize=0;
		for(int lev=levelMax;lev>=levelMin;lev--) {imageSizes[levelMax-lev]=imageSize/Math.pow(2,(lev-1));sumSize+=imageSizes[levelMax-lev];}
		double factorProcess=1E-8;
		double factorView=1E-7;
		double factorInit=2E-7;
		double bonusTime=factorInit*imageSize;
		double displayTime=nbIter*factorView*(levelMax-levelMin+1)*viewRegistrationLevel*imageSize;
		double processingTime=factorProcess*sumSize*nbIter;
		return (int)Math.round(processingTime+displayTime+bonusTime);
	}

	
	
	/**
	 * Medium level functions : constructor, and managers algorithms. The Manager Handling should follow this order (see below in the commentary)
	 * In the order :
	 * call the constructor
	 * setMovingImage(ijImgMov);
	 * setReferenceImage(ijImgMov);
	 * setMetric(MetricType metricType)
	 * (eventually) setCapillaryHandlingOn
	 * addStepToQueue( ... )
	 * addStepToQueue( ... )
	 * addStepToQueue( ... )
	 * register();
	 * ImagePlus resultat=computeRegisteredImage();
	 */
	public ItkRegistration() {
		this.registrationSummary=new ArrayList<ImagePlus>();
		this.metricType=null;
		this.transform=null;
		this.imgMovSuccessiveResults=new ArrayList<ImagePlus>();
		this.centerTransformFilter=new CenteredTransformInitializerFilter();
		this.gaussFilter=new RecursiveGaussianImageFilter();
		this.transformation3DTypes=new ArrayList<Transform3DType>();
		this.centeringStrategies=new ArrayList<CenteringStrategy>();
		this.nbLevels= new ArrayList<Integer> ();
		this.shrinkFactors= new ArrayList<int[]> ();
		this.dimensions= new ArrayList<int[][]>() ;
		this.sigmaFactors= new ArrayList<double[]> ();

		this.registrationMethods= new ArrayList<ImageRegistrationMethod> ();
		this.transformation3DTypes= new ArrayList<Transform3DType>() ;
		this.scalerTypes= new ArrayList<ScalerType>();
		this.weights= new ArrayList<double[]>() ;
		this.scales= new ArrayList<double[]>() ;

		this.currentLevel=0;
		this.zoomFactor=2;
		this.nbStep=0;
		this.currentStep=0;
		return;
	}

	public void addStepToQueue(int levelMin,int levelMax,double sigma, int iterations,    double learning_rate,  Transform3DType typeTransfo,double[]weights,
			OptimizerType optimizerType,ScalerType scalerType,double[]scales, 
			boolean doubleIterAtCoarsestLevels,CenteringStrategy centeringStrategy,SamplingStrategy samplingStrategy){


		int[]shrinkFactors=subSamplingFactorsAtSuccessiveLevels(levelMin,levelMax,doubleIterAtCoarsestLevels,this.basis);
		double[]sigmaFactors=sigmaFactorsAtSuccessiveLevels(voxelSizeReference,shrinkFactors,sigma);
		int[][]dimensions=imageDimsAtSuccessiveLevels(imageSizeReference,shrinkFactors);

		this.shrinkFactors.add(shrinkFactors);
		this.dimensions.add(dimensions);
		this.sigmaFactors.add(sigmaFactors);
		ImageRegistrationMethod reg=new ImageRegistrationMethod();
		reg.setShrinkFactorsPerLevel(ItkImagePlusInterface.intArrayToVectorUInt32(shrinkFactors));
		reg.setSmoothingSigmasAreSpecifiedInPhysicalUnits(true);
		reg.smoothingSigmasAreSpecifiedInPhysicalUnitsOn();
		reg.setSmoothingSigmasPerLevel(ItkImagePlusInterface.doubleArrayToVectorDouble(sigmaFactors));

		switch(metricType) {
		case JOINT:reg.setMetricAsJointHistogramMutualInformation();break;
		case MEANSQUARE:reg.setMetricAsMeanSquares();break;
		case CORRELATION:reg.setMetricAsCorrelation();break;
		case MATTES:reg.setMetricAsMattesMutualInformation(128);break;
		case DEMONS:reg.setMetricAsDemons();break;
		case ANTS:reg.setMetricAsANTSNeighborhoodCorrelation(3);break;
		default:reg.setMetricAsCorrelation();	break;			
		}

		double learningRate=learning_rate;
		double minStep = 0.001;
		int numberOfIterations = iterations;
		double relaxationFactor = 0.8;
		double convergenceMinimumValue=1E-6;
		int convergenceWindowSize=10;
		double stepLength=1;
		VectorUInt32 numberOfSteps=ItkImagePlusInterface.intArrayToVectorUInt32(new int[] {4,4,4});//Lets check that, one day.
		double simplexDelta=learning_rate;

		switch(optimizerType){
		case ITK_GRADIENT:reg.setOptimizerAsGradientDescent(learningRate/30.0, numberOfIterations, convergenceMinimumValue, convergenceWindowSize);break;
		case ITK_GRADIENT_REGULAR_STEP: reg.setOptimizerAsRegularStepGradientDescent(learningRate, minStep, numberOfIterations,relaxationFactor);break;
		case ITK_GRADIENT_LINE_SEARCH: reg.setOptimizerAsGradientDescentLineSearch(learningRate, numberOfIterations,convergenceMinimumValue, convergenceWindowSize);break;
		case ITK_GRADIENT_CONJUGATE: reg.setOptimizerAsConjugateGradientLineSearch(learningRate, numberOfIterations,convergenceMinimumValue, convergenceWindowSize);break;
		//case LBFGSB: reg.setOptimizerAsLBFGSB(gradientConvergenceTolerance);break;
		//case LBFGS2: reg.setOptimizerAsLBFGS2(solutionAccuracy);break;
		//case POWELL: reg.setOptimizerAsPowell(numberOfIterations, maximumLineIterations, stepLength,stepTolerance, valueTolerance);break;
		//case EVOLUTIONARY: reg.setOptimizerAsOnePlusOneEvolutionary(numberOfIterations);break;
		case ITK_EXHAUSTIVE: reg.setOptimizerAsExhaustive(numberOfSteps, stepLength);break;
		case ITK_AMOEBA: reg.setOptimizerAsAmoeba(simplexDelta, numberOfIterations);break;
		default: reg.setOptimizerAsAmoeba(simplexDelta, numberOfIterations);break;
		}

		switch(samplingStrategy) {
		case NONE: reg.setMetricSamplingStrategy(ImageRegistrationMethod.MetricSamplingStrategyType.NONE);break;
		case REGULAR: reg.setMetricSamplingStrategy(ImageRegistrationMethod.MetricSamplingStrategyType.REGULAR);break;
		case RANDOM: reg.setMetricSamplingStrategy(ImageRegistrationMethod.MetricSamplingStrategyType.RANDOM);break;
		}
		// For a test, one day : SetMetricSamplingPercentagePerLevel() : itk::simple::ImageRegistrationMethod


		this.transformation3DTypes.add(typeTransfo);
		this.scalerTypes.add(scalerType);
		this.scales.add(scales);
		this.weights.add(weights);
		this.centeringStrategies.add(centeringStrategy);
		this.registrationMethods.add(reg);
		nbStep++;
	}

	public void runNextStep(){
		if(this.transform==null && currentStep>0) { System.err.println("Pas de transformation calculee a l etape precedente. Exit");return;}
		boolean flagCentering=false;
		Image itkImgRefTrans=new Image(itkImgRef);
		Image itkImgMovTrans=new Image(itkImgMov);

		//Centering strategies
		switch(centeringStrategies.get(currentStep)) {
		case NONE: ;break;
		case IMAGE_CENTER: 
			centerTransformFilter.geometryOn();
			centerTransformFilter.setOperationMode(CenteredTransformInitializerFilter.OperationModeType.GEOMETRY);
			flagCentering=true;
			break;
		case MASS_CENTER: 
			centerTransformFilter.momentsOn();
			centerTransformFilter.setOperationMode(CenteredTransformInitializerFilter.OperationModeType.MOMENTS);
			flagCentering=true;
			break;
		}


		//Check transform
		ItkTransform trPlus=null;
		switch(transformation3DTypes.get(currentStep)) {
			case EULER: trPlus=new ItkTransform(new Euler3DTransform());break;
			case EULER2D: trPlus=new ItkTransform(new Euler2DTransform());break;
			case VERSOR:trPlus=new ItkTransform(new VersorRigid3DTransform());break;
			case TRANSLATION:trPlus=new ItkTransform(new TranslationTransform(3));break;
			case AFFINE:trPlus=new ItkTransform(new AffineTransform(3));break;
			case SIMILARITY:trPlus=new ItkTransform(new Similarity3DTransform());break;
			default:trPlus=new ItkTransform(new Euler3DTransform());break;
		}
		if(flagCentering && transformation3DTypes.get(currentStep)!= Transform3DType.TRANSLATION)trPlus=new ItkTransform(centerTransformFilter.execute(this.itkImgRef,this.itkImgMov,trPlus));

		if(this.transform==null)this.transform=trPlus;
		else this.transform.addTransform(trPlus);
		this.registrationMethods.get(currentStep).setInitialTransform(this.transform);	
		switch(scalerTypes.get(currentStep)) {
		case NONE: ;break;
		case MANUAL: this.registrationMethods.get(currentStep).setOptimizerScales(ItkImagePlusInterface.doubleArrayToVectorDouble(scales.get(currentStep)));break;
		case SCALER_INDEX: this.registrationMethods.get(currentStep).setOptimizerScalesFromIndexShift();break;
		case SCALER_PHYSICAL: this.registrationMethods.get(currentStep).setOptimizerScalesFromPhysicalShift();break;
		case JACOBIAN_VERSOR: this.registrationMethods.get(currentStep).setOptimizerScalesFromJacobian();break;
		}

		// PARAMETERS WEIGHTING FOR FOSTERING SOME OR SOME BEHAVIOUR //////////////	
		if(this.weights.get(this.currentStep)!=null && this.weights.get(this.currentStep).length>0) {
			this.registrationMethods.get(currentStep).setOptimizerWeights(ItkImagePlusInterface.doubleArrayToVectorDouble(this.weights.get(currentStep)));		
		}

 		//////////// GO ! ////////////////
		this.registrationThread= new Thread() {  { setPriority(Thread.NORM_PRIORITY); }  
			public void run() {  
				try {
					registrationMethods.get(currentStep).execute(itkImgRefTrans,itkImgMovTrans);
					}catch(Exception e) {System.out.println("Interruption of Itk registration");itkRegistrationInterrupted=true;}
			}
		};
		VitimageUtils.startAndJoin(this.registrationThread);
		if(itkRegistrationInterrupted) {
			itkIsInterruptedSucceeded=true;
			this.currentStep=100000;
		}
		else this.currentStep++;
	}

	public void register(){
		this.currentStep=0;
		while(currentStep<nbStep) {
			int excludeMargin=ijImgRef.getStackSize()/4;
			this.registrationMethods.get(currentStep).setMetricFixedMask(ItkImagePlusInterface.imagePlusToItkImage(VitimageUtils.restrictionMaskForFadingHandling(this.ijImgRef,excludeMargin)));
			this.registrationMethods.get(currentStep).setMetricMovingMask(ItkImagePlusInterface.imagePlusToItkImage(VitimageUtils.restrictionMaskForFadingHandling(this.ijImgMov,excludeMargin)));

			this.createUpdater();
			updateView(this.dimensions.get(0)[0],this.sigmaFactors.get(0)[0],this.shrinkFactors.get(0)[0],
						"Position before registration, Red=Ref, Green=Mov",this.transform==null ? new ItkTransform() : this.transform);
			this.runNextStep();
			if(this.displayRegistration>0) {
				this.resampler.setTransform(this.transform);
				ImagePlus temp=ItkImagePlusInterface.itkImageToImagePlus(this.resampler.execute(this.itkImgMov));
				this.imgMovSuccessiveResults.add(temp);
			}

		}
		displayEndOfRegistrationMessage();
		if(this.displayRegistration>0) {
			this.sliceView.changes=false;
			this.sliceView.close();
		}
	}

	
	
	
	/**
	 * Functions for displaying, tracking and keep memories of registration results along the computation
	 */
	public void displayEndOfRegistrationMessage() {
		IJ.log("-----------------------------------------");
		IJ.log("-----------------------------------------");
		IJ.log("------     End of registration    -------");
		IJ.log("-----------------------------------------");
		IJ.log("Optimizer stop condition: "+registrationMethods.get(nbStep-1).getOptimizerStopConditionDescription()+"\n");
		IJ.log(" Iteration: "+registrationMethods.get(nbStep-1).getOptimizerIteration()+"\n");
		IJ.log(" Metric value: "+registrationMethods.get(nbStep-1).getMetricValue()+"\n");
	}

	public ImagePlus computeRegisteredImage() {
		if(transform==null)return null;
		ResampleImageFilter resampler = new ResampleImageFilter();
		resampler.setReferenceImage(itkImgRef);
		resampler.setDefaultPixelValue(0);
		resampler.setTransform(transform);
		Image imgResultat=resampler.execute(itkImgMov);
		ImagePlus res=ItkImagePlusInterface.itkImageToImagePlus(imgResultat);
		res.getProcessor().resetMinAndMax();
		return res;
	}

	public void updateView(int []dimensions,double sigmaFactor,int shrinkFactor,String viewText,ItkTransform currentTrans) {
		if(this.displayRegistration==0)return;
		this.gaussFilter.setSigma(sigmaFactor);
		VectorDouble vectVoxSizes=new VectorDouble(3);
		vectVoxSizes.set(0,this.voxelSizeReference[0]*this.imageSizeReference[0]/dimensions[0]);
		vectVoxSizes.set(1,this.voxelSizeReference[1]*this.imageSizeReference[1]/dimensions[1]);
		vectVoxSizes.set(2,this.voxelSizeReference[2]*this.imageSizeReference[2]/dimensions[2]);

		//Update reference viewing image and the viewing slice, if needed
		this.resampler=new ResampleImageFilter();
		this.resampler.setDefaultPixelValue(0);
		this.resampler.setTransform(ItkTransform.getTransformForResampling(this.voxelSizeReference, VitimageUtils.getVoxelSizes(this.ijImgMov)));
		if(this.lookLikeOptimizerLooks) {
			this.resampler.setOutputSpacing(vectVoxSizes);
			this.resampler.setSize(ItkImagePlusInterface.intArrayToVectorUInt32(dimensions));
		}
		else {
			this.resampler.setOutputSpacing(ItkImagePlusInterface.doubleArrayToVectorDouble(this.voxelSizeReference));
			this.resampler.setSize(ItkImagePlusInterface.intArrayToVectorUInt32(this.imageSizeReference));
		}
		this.itkImgViewRef=this.resampler.execute(this.itkImgRef);
		if(this.lookLikeOptimizerLooks) {
			for(int i=0;i<3;i++) {
				if(this.imageSizeReference[i]>=4) {
					this.gaussFilter.setDirection(i);
					itkImgViewRef=this.gaussFilter.execute(this.itkImgViewRef);			
				}
			}
		}
		this.sliceViewRef=ItkImagePlusInterface.itkImageToImagePlusSlice(this.itkImgViewRef,(int)Math.ceil(this.viewSlice*1.0/(this.lookLikeOptimizerLooks ? shrinkFactor : 1)));
		if(this.flagRange)this.sliceViewRef.setDisplayRange(this.refRange[0], this.refRange[1]);
		//Update moving image
		this.resampler=new ResampleImageFilter();
		this.resampler.setDefaultPixelValue(0);
		if(this.lookLikeOptimizerLooks) {
			this.resampler.setOutputSpacing(vectVoxSizes);
			this.resampler.setSize(ItkImagePlusInterface.intArrayToVectorUInt32(dimensions));
		}
		else {
			this.resampler.setOutputSpacing(ItkImagePlusInterface.doubleArrayToVectorDouble(this.voxelSizeReference));
			this.resampler.setSize(ItkImagePlusInterface.intArrayToVectorUInt32(this.imageSizeReference));			
		}
		if(this.transform!=null)this.resampler.setTransform(this.transform);
		else this.resampler.setTransform(ItkTransform.getTransformForResampling(this.voxelSizeReference, VitimageUtils.getVoxelSizes(this.ijImgMov)));
		this.itkImgViewMov=this.resampler.execute(this.itkImgMov);
		if(this.lookLikeOptimizerLooks) {
			for(int i=0;i<3;i++) {
				if(this.imageSizeReference[i]>=4) {
					this.gaussFilter.setDirection(i);
					itkImgViewRef=this.gaussFilter.execute(this.itkImgViewRef);	
				}
			}
		}
		this.sliceViewMov=ItkImagePlusInterface.itkImageToImagePlusSlice(this.itkImgViewMov,(int)Math.ceil(this.viewSlice*1.0/(this.lookLikeOptimizerLooks ? shrinkFactor : 1)));
		if(this.flagRange)this.sliceViewMov.setDisplayRange(this.movRange[0], this.movRange[1]);

		//Compose the images
		if(this.sliceView==null || this.sliceViewRef.getWidth() != sliceView.getWidth()) {
			if(this.sliceView!=null) {this.sliceView.changes=false;this.sliceView.close();}
			if(flagRange)this.sliceView=VitimageUtils.compositeNoAdjustOf(this.sliceViewRef,this.sliceViewMov,"Registration is running. Red=Reference, Green=moving");
			else this.sliceView=VitimageUtils.compositeOf(this.sliceViewRef,this.sliceViewMov,"Registration is running. Red=Reference, Green=moving");
			this.sliceView.show();
			this.sliceView.getWindow().setSize(this.viewWidth,this.viewHeight);
			this.sliceView.getCanvas().fitToWindow();	
		}
		else {//Copie en place
			ImagePlus temp=null;
			if(flagRange)temp=VitimageUtils.compositeNoAdjustOf(this.sliceViewRef,this.sliceViewMov,"Red=Reference, Green=moving");
			else temp=VitimageUtils.compositeOf(this.sliceViewRef,this.sliceViewMov,"Red=Reference, Green=moving");
			temp=VitimageUtils.writeTextOnImage(viewText,temp,this.fontSize*temp.getWidth()/this.imageSizeReference[0],0);
			temp=VitimageUtils.writeTextOnImage(currentTrans.drawableString(),temp,this.fontSize*temp.getWidth()/this.imageSizeReference[0]-2,1);
			IJ.run(this.sliceView, "Select All", "");
			IJ.run(temp, "Select All", "");
			temp.copy();
			this.sliceView.paste();			
		}

		//Prepare slices for summary 
		this.resampler=new ResampleImageFilter();
		this.resampler.setDefaultPixelValue(0);
		this.resampler.setOutputSpacing(ItkImagePlusInterface.doubleArrayToVectorDouble(this.voxelSizeReference));
		this.resampler.setSize(ItkImagePlusInterface.intArrayToVectorUInt32(this.imageSizeReference));
		this.resampler.setTransform(ItkTransform.getTransformForResampling(this.voxelSizeReference, this.voxelSizeReference));
		this.itkSummaryRef=this.resampler.execute(this.itkImgViewRef);
		this.itkSummaryMov=this.resampler.execute(this.itkImgViewMov);
		if(movie3D) {
			this.sliceSummaryMov=ItkImagePlusInterface.itkImageToImagePlus(this.itkSummaryMov);
			this.sliceSummaryRef=ItkImagePlusInterface.itkImageToImagePlus(this.itkSummaryRef);
		}
		else {
			this.sliceSummaryMov=ItkImagePlusInterface.itkImageToImagePlusSlice(this.itkSummaryMov,this.viewSlice);
			this.sliceSummaryRef=ItkImagePlusInterface.itkImageToImagePlusSlice(this.itkSummaryRef,this.viewSlice);
		}
		/*this.sliceSummaryRef.getProcessor().resetMinAndMax();
		this.sliceSummaryMov.getProcessor().resetMinAndMax();
		IJ.run(this.sliceSummaryRef,"8-bit","");
		IJ.run(this.sliceSummaryMov,"8-bit","");*/
		ImagePlus temp2=VitimageUtils.compositeOf(this.sliceSummaryRef,this.sliceSummaryMov,"Registration is running. Red=Reference, Green=moving");
		temp2=VitimageUtils.writeTextOnImage(viewText,temp2,this.fontSize*temp2.getWidth()/this.imageSizeReference[0],0);
		temp2=VitimageUtils.writeTextOnImage(currentTrans.drawableString(),temp2,this.fontSize*temp2.getWidth()/this.imageSizeReference[0]-2,1);
		this.registrationSummary.add(temp2);
	}

	public void setTextInfoAtEachIterationOn() {
		textInfoAtEachIteration=true;
	}
	
	public void setTextInfoAtEachIterationOff() {
		textInfoAtEachIteration=false;
	}
	

	
	

	/**
	 * Initializers
	 */
	public void setReferenceImage(ImagePlus imgIn) {
		ImagePlus img=null;
		if(imgIn.getType()==ImagePlus.GRAY32)img=VitimageUtils.imageCopy(imgIn);
		else if(imgIn.getType()==ImagePlus.GRAY16)img=VitimageUtils.convertShortToFloatWithoutDynamicChanges(imgIn);
		else if(imgIn.getType()==ImagePlus.GRAY8)img=VitimageUtils.convertByteToFloatWithoutDynamicChanges(imgIn);
		else IJ.log("Warning : unusual type of image in ITKRegistrationManager.setReferenceImage : "+imgIn.getType()+" . Registration will fail shortly");
		this.ijImgRef=VitimageUtils.imageCopy(img);
		this.viewHeight=ijImgRef.getHeight()*zoomFactor;
		this.viewWidth=ijImgRef.getWidth()*zoomFactor;
		this.itkImgRef=ItkImagePlusInterface.imagePlusToItkImage(ijImgRef);
		this.imageSizeReference=new int[] {ijImgRef.getWidth(),ijImgRef.getHeight(),ijImgRef.getStackSize()};
		this.voxelSizeReference=new double[] {ijImgRef.getCalibration().pixelWidth,ijImgRef.getCalibration().pixelHeight,ijImgRef.getCalibration().pixelDepth};
		this.viewSlice=(int)Math.round(ijImgRef.getStackSize()/2.0);
	}

	public void setViewSlice(int slic) {
		this.viewSlice=slic;		
	}
	
	public void setMovingImage(ImagePlus imgIn) {
		ImagePlus img=null;
		VitimageUtils.printImageResume(imgIn);
		if(imgIn.getType()==ImagePlus.GRAY32)img=VitimageUtils.imageCopy(imgIn);
		else if(imgIn.getType()==ImagePlus.GRAY16)img=VitimageUtils.convertShortToFloatWithoutDynamicChanges(imgIn);
		else if(imgIn.getType()==ImagePlus.GRAY8) {img=VitimageUtils.convertByteToFloatWithoutDynamicChanges(imgIn);}
		else IJ.log("Warning : unusual type of image in ITKRegistrationManager.setMovingImage : "+imgIn.getType()+" . Registration will fail shortly");
		this.ijImgMov=VitimageUtils.imageCopy(img);
		this.itkImgMov=ItkImagePlusInterface.imagePlusToItkImage(ijImgMov);
		
	}

	public void setMetric(MetricType metricType) {
		this.metricType=metricType;
	}

	public void setInitialTransformation(ItkTransform trans) {
		if(this.transform !=null || this.currentStep>0) System.err.println("Une transformation initiale est deja existante");
		else this.transform=new ItkTransform(trans);
	}

	public void createUpdater() {
		this.updater=new IterationUpdate(this,this.registrationMethods.get(currentStep));
		this.registrationMethods.get(this.currentStep).removeAllCommands();
		this.registrationMethods.get(this.currentStep).addCommand(EventEnum.sitkIterationEvent,this.updater);
	}






	/**
	 * Helper functions to build the pyramidal scheme based on few parameters
	 */
	public int[] subSamplingFactorsAtSuccessiveLevels(int levelMin,int levelMax,boolean doubleIterAtCoarsestLevels,double basis){
		if(levelMax<levelMin)levelMax=levelMin;
		if(levelMin<=0)return null;
		int nbLevels=levelMax-levelMin+1;
		int nbDouble=doubleIterAtCoarsestLevels ? (nbLevels>2 ? nbLevels-2 : 0) : 0;
		int nbTot=nbLevels+nbDouble;
		int []ret=new int[nbTot];
		for(int i=0;i<2 && i<nbTot;i++) {
				ret[nbTot-1-i]=(int)Math.round(Math.pow(basis,(levelMin-1+i)));
		}
		if(doubleIterAtCoarsestLevels) {
			for(int i=0;i<(nbTot-2)/2;i++) {
				ret[nbTot-1-(2+i*2)]=(int)Math.round(Math.pow(basis,(levelMin-1+i+2))) ;
				ret[nbTot-1-(2+i*2+1)]= (int)Math.round(Math.pow(basis,(levelMin-1+i+2)));
				
			}
		}
		else {
			for(int i=2;i<nbTot;i++) {
					ret[nbTot-1-i]=(int)Math.round(Math.pow(basis,(levelMin-1+i))) ;
			}

		}		
		return ret;
	}

	public int [][] imageDimsAtSuccessiveLevels(int []dimsImg,int []subFactors) {		
		if (subFactors==null)return null;
		int n=subFactors.length;
		int [][]ret=new int[n][3];
		for(int i=0;i<n;i++) for(int j=0;j<3;j++)ret[i][j]=(int)Math.ceil(dimsImg[j]/subFactors[i]);
		return ret;
	}

	public double[] sigmaFactorsAtSuccessiveLevels(double []voxSize,int[]subFactors,double rapportSigma) {
		if (subFactors==null)return null;
		double[]ret=new double[subFactors.length];
		for(int i=0;i<subFactors.length;i++) {
			double voxSizeMin=Math.min(Math.min(voxSize[0]*subFactors[i],voxSize[1]*subFactors[i]),voxSize[2]*subFactors[i]);
			ret[i]=voxSizeMin*rapportSigma;
		}
		return ret;
	}




	/**
	 * Minor getters/setters
	 */
	public ArrayList<Integer> getNbLevels() {
		return nbLevels;
	}

	public void setNbLevels(ArrayList<Integer> nbLevels) {
		this.nbLevels = nbLevels;
	}

	public int[] getCurrentShrinkFactors() {
		return shrinkFactors.get(currentStep);
	}

	public void setShrinkFactors(ArrayList<int[]> shrinkFactors) {
		this.shrinkFactors = shrinkFactors;
	}

	public int[][] getCurrentDimensions() {
		return dimensions.get(currentStep);
	}

	public double[] getCurrentSigmaFactors() {
		return sigmaFactors.get(currentStep);
	}

	public int getCurrentLevel() {
		return currentLevel;
	}

	public void setCurrentLevel(int currentLevel) {
		this.currentLevel = currentLevel;
	}

	public ArrayList<ScalerType> getScalerTypes() {
		return scalerTypes;
	}

	public void setScalerTypes(ArrayList<ScalerType> scalerTypes) {
		this.scalerTypes = scalerTypes;
	}

	public int getNbSteps() {
		return nbStep;
	}

	public void setNbSteps(int nbStep) {
		this.nbStep = nbStep;
	}

	public int getCurrentStep() {
		return currentStep;
	}

	public void setCurrentStep(int currentStep) {
		this.currentStep = currentStep;
	}

	public ArrayList<double[]> getWeights() {
		return weights;
	}

	public void setWeights(ArrayList<double[]> weights) {
		this.weights = weights;
	}

	public ArrayList<double[]> getScales() {
		return scales;
	}

	public void setScales(ArrayList<double[]> scales) {
		this.scales = scales;
	}

	public ItkTransform getCurrentTransform() {
		return new ItkTransform(this.transform);
	}
	

	
}
	

/**
 * Listener for gathering optimizer events. It allows the manager to update and display the process state along the running
 */
class IterationUpdate  extends Command {
	private double initScore=1;
	private ImageRegistrationMethod method;
	private ItkRegistration manager;
	private int [] tabShrink;
	private double refreshingPeriod=50;
	private int  [][]tabSizes;
	private double[] tabSigma;
	private long memoirePyramide=1000;
	private double timeStamp1=0;
	private double timeStamp0=0;
	private double timeStampInit=0;
	private double durationIter=0;
	private double durationTot=0;
	private double nextViewTime=0+refreshingPeriod;
	private double improvement=0;
	public IterationUpdate(ItkRegistration manager,ImageRegistrationMethod method) {
		super();
		this.manager=manager;
		this.tabSigma=manager.getCurrentSigmaFactors();
		this.tabShrink=manager.getCurrentShrinkFactors();
		this.tabSizes=manager.getCurrentDimensions();
		this.method=method;
		timeStamp1=0;
		timeStamp0=0;
		timeStampInit=0;
		durationTot=0;
		durationIter=0;
		
	}

	public void execute() {
		boolean isNewLevel=(method.getOptimizerIteration()<memoirePyramide);		  
		int mem=(int) method.getCurrentLevel();

		if(isNewLevel) {
			String st="";
			if(memoirePyramide<1000) {
				for(int i=0;i<mem-1;i++)st+="     ";
				st+="---------\n";
				for(int i=0;i<mem-1;i++)st+="     ";
				st+="Level "+(mem-1)+" finished. Going to next level\n\n\n\n";
				for(int i=0;i<mem;i++)st+="     ";
			}
			st+="Level "+(mem+1)+" / "+tabShrink.length+" .\n Sigma for smoothing = "+(VitimageUtils.dou(tabSigma[mem]))+" mm . Subsampling factor = "+tabShrink[(int) mem]+
					" .  Image size = "+tabSizes[mem][0]+" x "+tabSizes[mem][1]+" x "+tabSizes[mem][2]+" . Execution with "+method.getNumberOfThreads()+" threads. Starting.\n";
			for(int i=0;i<mem;i++)st+="     ";
			st+="----------";		  
			IJ.log(st);		  
			//IJ.log(st);
		}
		memoirePyramide=method.getOptimizerIteration();
		String pyr="";
		for(int i=1;i<=method.getCurrentLevel();i++)pyr+="     ";
		pyr+="Step "+(manager.getCurrentStep()+1)+"/"+manager.getNbSteps()+" | Level "+(method.getCurrentLevel()+1)+"/"+tabSigma.length+" | ";
		if(timeStamp0==0)  timeStampInit=System.nanoTime()*1.0/1000000.0;
		timeStamp0=timeStamp1;
		timeStamp1=System.nanoTime()*1.0/1000000.0;
		durationIter=(timeStamp0 !=0 ? timeStamp1-timeStamp0 : 0);
		durationTot=(timeStamp0 !=0 ? timeStamp1-timeStampInit : 0)/1000.0;
		double durIter=(durationIter<1000 ? durationIter : durationIter/1000.0);
		String unitIter=(durationIter<1000 ? "ms" : "s ");
		double durTot=(durationTot<180 ? durationTot : durationTot/60);
		String unitTot=(durationTot<180 ? "s " : "mn");
		durationTot=(int)Math.round(timeStamp0 !=0 ? timeStamp1-timeStampInit : 0);
		if(isNewLevel)initScore=-100.0*method.getMetricValue();
		improvement=Math.abs((-100.0*method.getMetricValue() - initScore)/initScore)*100;
		if(method.getOptimizerIteration()==0)System.out.format("%sIteration %3d  |  Score = %6.4f  |  Titeration = %8.4f %s  |  Ttotal = %5.2f %s  | Improvement = %4.2f |\n",
				pyr,method.getOptimizerIteration()
				,-100.0*method.getMetricValue()
				, (float)durIter,unitIter
				, (float)durTot,unitTot,improvement
				);
		else if(method.getOptimizerIteration()%(manager.textInfoAtEachIteration ? 1 :  10    )==0)System.out.format("%sIteration %3d  |  Score = %6.4f  |  Titeration = %8.4f %s  |  Ttotal = %5.2f %s  | Evolution = %4.2f%% |\n",
				pyr,method.getOptimizerIteration()
				,-100.0*method.getMetricValue()
				, (float)durIter,unitIter
				, (float)durTot,unitTot,improvement
				);
		if(durationTot>nextViewTime) {
			nextViewTime=durationTot+refreshingPeriod;
			String st=String.format("Step=%1d/%1d - Level=%1d/%1d - Iter=%3d - Score=%6.4f - Evolution=%4.2f%%",
					(manager.getCurrentStep()+1),
					manager.getNbSteps(),
					(method.getCurrentLevel()+1),tabSigma.length,method.getOptimizerIteration(),-100.0*method.getMetricValue(),improvement);
			this.manager.updateView(this.tabSizes[mem],tabSigma[mem],this.tabShrink[mem],st,new ItkTransform(method.getInitialTransform()));
		}
	}

}
