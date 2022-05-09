package fr.cirad.image.registration;
import java.util.ArrayList;
import java.util.Random;

import org.itk.simple.ComposeImageFilter;
import org.itk.simple.DisplacementFieldJacobianDeterminantFilter;
import org.itk.simple.DisplacementFieldTransform;
import org.itk.simple.Image;
import org.itk.simple.ImageFileReader;
import org.itk.simple.ImageFileWriter;
import org.itk.simple.MultiplyImageFilter;
import org.itk.simple.ResampleImageFilter;
import org.itk.simple.SimpleITK;
import org.itk.simple.Transform;
import org.itk.simple.VectorDouble;
import org.itk.simple.VectorIndexSelectionCastImageFilter;
import org.scijava.java3d.Transform3D;

import fr.cirad.image.registration.ItkTransform;

import fr.cirad.image.common.ItkImagePlusInterface;
import fr.cirad.image.common.Timer;
import fr.cirad.image.common.TransformUtils;
import fr.cirad.image.common.VitiDialogs;
import fr.cirad.image.common.VitimageUtils;
import ij.IJ;
import ij.ImagePlus;
import ij.plugin.ChannelSplitter;
import ij.plugin.Concatenator;
import ij.plugin.Duplicator;
import ij.plugin.HyperStackConverter;
import ij.plugin.RGBStackMerge;
import ij.process.ImageProcessor;
import ij.process.LUT;
import math3d.Point3d;
import vib.FastMatrix;

public class ItkTransform extends Transform implements ItkImagePlusInterface{
	private boolean isDense=false;
	private boolean isFlattened=true;
	public int step=0;


	/* Constructors and factories*/
	public ItkTransform(){
		super();
	}
	
	public ItkTransform(ItkTransform model) {		
		super(model);
		this.isDense=model.isDense;
		this.isFlattened=model.isFlattened;
		return;
	}

	public static ItkTransform itkTransformFromCoefs(double[]coefs) {
		org.itk.simple.AffineTransform aff=new org.itk.simple.AffineTransform( ItkImagePlusInterface.doubleArrayToVectorDouble(new double[] { coefs[0] , coefs[1] , coefs[2] ,      coefs[4] , coefs[5] , coefs[6] ,   coefs[8] , coefs[9] , coefs[10] } ),    
				ItkImagePlusInterface.doubleArrayToVectorDouble( new double[] { coefs[3] , coefs[7] , coefs[11] } ), ItkImagePlusInterface.doubleArrayToVectorDouble(new double[] {0,0,0} ) );
		return new ItkTransform(aff);
	}
	
	public static ItkTransform itkTransformFromDICOMVectors(double[]vx,double[]vy,double[]vz,double[]t) {
		double []vzz=TransformUtils.vectorialProduct(new double[] {  vx[0] , vy[0] , vz[0]}, new double[] {-vx[1] ,- vy[1] , -vz[1] });
//		return itkTransformFromCoefs(new double[] { vx[0] , -vx[1] , -vx[2] , t[0] ,          vy[0] , -vy[1] , -vy[2] , t[1] ,        vzz[0] , vzz[1] , vzz[2] , t[2]   });
		return itkTransformFromCoefs(new double[] { vx[0] , vy[0] , vz[0] , t[0] ,          -vx[1] ,- vy[1] , -vz[1] , -t[1] ,        vzz[0] , vzz[1] , vzz[0] , -t[2]   });
	}

	public static ItkTransform itkTransformFromDICOMVectorsAXIAL(double[]vx,double[]vy,double[]vz,double[]t) {
		double []vzz=TransformUtils.vectorialProduct(new double[] {  vx[0] , vy[0] , vz[0]}, new double[] {-vx[1] ,- vy[1] , -vz[1] });
//		return itkTransformFromCoefs(new double[] { vx[0] , -vx[1] , -vx[2] , t[0] ,          vy[0] , -vy[1] , -vy[2] , t[1] ,        vzz[0] , vzz[1] , vzz[2] , t[2]   });
		return itkTransformFromCoefs(new double[] { vx[0] , vy[0] , vz[0] , t[0] +40.63,          -vx[1] ,- vy[1] , -vz[1] , -t[1]+50.7 ,        vzz[0] , vzz[1] , vzz[2] , -t[2] +213.5  });
	}
		
	public static ItkTransform itkTransformFromDICOMVectorsNOAXIAL(double[]vx,double[]vy,double[]vz,double[]t) {
		double []vzz=TransformUtils.vectorialProduct(new double[] {  vx[0] , vy[0] , vz[0]}, new double[] {-vx[1] ,- vy[1] , -vz[1] });
//		return itkTransformFromCoefs(new double[] { vx[0] , -vx[1] , -vx[2] , t[0] ,          vy[0] , -vy[1] , -vy[2] , t[1] ,        vzz[0] , vzz[1] , vzz[2] , t[2]   });
		return itkTransformFromCoefs(new double[] { vx[0] , vy[0] , vz[0] , t[0] ,          -vx[1] ,- vy[1] , -vz[1] , -t[1] ,        vzz[0] , vzz[1] , vzz[2] , -t[2]   });
	}
		
	public static ItkTransform getIdentityDenseFieldTransform(ImagePlus imgRef) {
		ImagePlus img=imgRef.duplicate();
		IJ.run(img,"32-bit","");
		for(int i=0;i<img.getNSlices();i++)img.getStack().getProcessor(i+1).set(0);
		return new ItkTransform(new DisplacementFieldTransform(ItkImagePlusInterface.convertImagePlusArrayToDisplacementField(new ImagePlus[] {img,img,img})));
	}
	


	
	
	
	
	
	/* Conversions of Transformations*/	

	public static Transform3D itkTransformToIj3dTransform(ItkTransform tr) {
		double[]tab=tr.toAffineArrayMonolineRepresentation();
		Transform3D ret=new Transform3D();
		ret.set(tab);
		return ret;
	}

	public static ItkTransform ij3dTransformToItkTransform(Transform3D tr) {
		double[]tab=new double[16];
		tr.get(tab);
		ItkTransform itkTr=itkTransformFromCoefs(tab);
		return itkTr;
	}

	public static ItkTransform fastMatrixToItkTransform(FastMatrix fm) {
		double[]tab=fm.rowwise16();
		org.itk.simple.AffineTransform aff=new org.itk.simple.AffineTransform(
				ItkImagePlusInterface.doubleArrayToVectorDouble(new double[] {tab[0],tab[1],tab[2],  tab[4],tab[5],tab[6],    tab[8],tab[9],tab[10] } ),
				ItkImagePlusInterface.doubleArrayToVectorDouble(new double[] {tab[3],tab[7],tab[11] } ),   ItkImagePlusInterface.doubleArrayToVectorDouble(   new double[] {0,0,0}  )  );
		return new ItkTransform(aff);
	}

	public ItkTransform(org.itk.simple.Transform tr) {
		super(tr);
		this.isDense=!tr.isLinear();
		return ;
	}

	public static ItkTransform array16ElementsToItkTransform(double[] tab) {
		org.itk.simple.AffineTransform aff=new org.itk.simple.AffineTransform(
				ItkImagePlusInterface.doubleArrayToVectorDouble(new double[] {tab[0],tab[1],tab[2], tab[4],tab[5],tab[6],    tab[8],tab[9],tab[10] } ),
				ItkImagePlusInterface.doubleArrayToVectorDouble(new double[] {tab[3],tab[7],tab[11]} ),   ItkImagePlusInterface.doubleArrayToVectorDouble(   new double[] {0,0,0}  )  );
		return new ItkTransform(aff);
	}


	public double[] toAffineArrayMonolineRepresentation() {
		double [][]tabTemp=toAffineArrayRepresentation();
		return new double[] {   tabTemp[0][0] , tabTemp[0][1] , tabTemp[0][2] , tabTemp[0][3] , 
								tabTemp[1][0] , tabTemp[1][1] , tabTemp[1][2] , tabTemp[1][3] , 
								tabTemp[2][0] , tabTemp[2][1] , tabTemp[2][2] , tabTemp[2][3] , 
								tabTemp[3][0] , tabTemp[3][1] , tabTemp[3][2] , tabTemp[3][3] };
	}

	public double[][] toAffineArrayRepresentation() {
		Point3d pt0=new Point3d(0,0,0);
		Point3d pt0Tr=this.transformPoint(pt0);
		Point3d pt1=new Point3d(1,0,0);
		Point3d pt1Tr=this.transformPoint(pt1);
		Point3d pt2=new Point3d(0,1,0);
		Point3d pt2Tr=this.transformPoint(pt2);
		Point3d pt3=new Point3d(0,0,1);
		Point3d pt3Tr=this.transformPoint(pt3);
		return new double[][] {    { pt1Tr.x-pt0Tr.x , pt2Tr.x-pt0Tr.x , pt3Tr.x-pt0Tr.x   ,pt0Tr.x    },    
											   { pt1Tr.y-pt0Tr.y , pt2Tr.y-pt0Tr.y , pt3Tr.y-pt0Tr.y   ,pt0Tr.y    },  
											   { pt1Tr.z-pt0Tr.z , pt2Tr.z-pt0Tr.z , pt3Tr.z-pt0Tr.z   ,pt0Tr.z    },  
											   { 0 , 0 , 0 , 1 }   };
	}

	
	
	public static double[]getImageCenter(ImagePlus img){
		double[]vals=VitimageUtils.getDimensionsRealSpace(img);
		vals[0]/=2;		vals[1]/=2;		vals[2]/=2;
		return vals;
	}
	
	

	/* Estimation of transformations from point set or euler angles*/	
	public static ItkTransform estimateBestAffine3D(Point3d[]setRef,Point3d[]setMov) {
		return fastMatrixToItkTransform(FastMatrix.bestLinear( setMov, setRef));
	}
		
	public static ItkTransform estimateBestRigid3D(Point3d[]setRef,Point3d[]setMov) {
		return fastMatrixToItkTransform(FastMatrix.bestRigid( setMov, setRef, false ));
	}

	public static ItkTransform estimateBestDense3D(Point3d[]setRef,Point3d[]setMov,ImagePlus imgRef,double sigma) {
		return new ItkTransform(new DisplacementFieldTransform(computeDenseFieldFromSparseCorrespondancePoints(new Point3d[][] {setMov,setRef},imgRef,sigma,true)));
	}

	
	public static ItkTransform estimateBestTranslation3D(Point3d[]setRef,Point3d[]setMov) {
		double dx=0,dy=0,dz=0;
		for(int i=0;i<setRef.length;i++) {
			dx+=(setRef[i].x-setMov[i].x);
			dy+=(setRef[i].y-setMov[i].y);
			dz+=(setRef[i].z-setMov[i].z);
		}
		return array16ElementsToItkTransform(new double[] {1,0,0,dx/setRef.length,  0,1,0,dy/setRef.length,  0,0,1,dz/setRef.length,  0,0,0,1});
	}

	
	
	public static ItkTransform estimateBestSimilarity3D(Point3d[]setRef,Point3d[]setMov) {
		FastMatrix fm=FastMatrix.bestRigid( setMov, setRef, true );
		IJ.log("Similarity transform computed. Coefficient of dilation : "+Math.pow(fm.det(),0.333333));
		return fastMatrixToItkTransform(fm);
	}

	//Angles are in radians
	public static ItkTransform getRigidTransform(double []center,double[]angles,double[]translation) {
		org.itk.simple.VectorDouble cent=ItkImagePlusInterface.doubleArrayToVectorDouble(center);
		org.itk.simple.VectorDouble trans=ItkImagePlusInterface.doubleArrayToVectorDouble(translation);		
		return new ItkTransform(new org.itk.simple.Transform(new org.itk.simple.Euler3DTransform (cent,angles[0],angles[1],angles[2], trans)));
	}

	public static ItkTransform getTransformForResampling(double[]voxSRef,double[]voxSMov) {
		double[]mat=new double[] {  1, 0, 0, 0.5*(voxSRef[0]-voxSMov[0]) ,
				0, 1, 0, 0.5*(voxSRef[1]-voxSMov[1]) ,
				0, 0, 1, 0.5*(voxSRef[2]-voxSMov[2]) };
		return ItkTransform.itkTransformFromCoefs(mat);
	}
		
	/*Building a smooth deformation field from correspondance points
	 * Description of correspondance points are in SI units, as following :
	 * corr[0][i]=original coordinates
	 * corr[1][i]=target coordinates
	 */
	public static Image computeDenseFieldFromSparseCorrespondancePoints(Point3d[][]correspondancePoints,ImagePlus imgRef,double sigma,boolean zeroPaddingOutside) {
		double epsilon = 10E-20;
		double []voxSizes=VitimageUtils.getVoxelSizes(imgRef);
		int []dimensions=VitimageUtils.getDimensions(imgRef);
		int nPt=correspondancePoints[0].length;
		int [][]vectPoints=new int[nPt][3];
		double [][]vectVals=new double[nPt][3];
		for(int i=0;i<vectPoints.length;i++) {
			vectPoints[i][0]=(int)Math.round(correspondancePoints[0][i].x/voxSizes[0]);
			vectPoints[i][1]=(int)Math.round(correspondancePoints[0][i].y/voxSizes[1]);
			vectPoints[i][2]=(int)Math.round(correspondancePoints[0][i].z/voxSizes[2]);
			vectVals[i][0]=correspondancePoints[1][i].x-correspondancePoints[0][i].x;
			vectVals[i][1]=correspondancePoints[1][i].y-correspondancePoints[0][i].y;
			vectVals[i][2]=correspondancePoints[1][i].z-correspondancePoints[0][i].z;
		}
		
		//Build weights image, and X,Y,Z components images
		ImagePlus imgWeights=IJ.createImage("tempW", dimensions[0], dimensions[1], dimensions[2], 32);
		ImagePlus imgFieldX=IJ.createImage("tempX", dimensions[0], dimensions[1], dimensions[2], 32);
		ImagePlus imgFieldY=IJ.createImage("tempY", dimensions[0], dimensions[1], dimensions[2], 32);
		ImagePlus imgFieldZ=IJ.createImage("tempZ", dimensions[0], dimensions[1], dimensions[2], 32);
		VitimageUtils.adjustImageCalibration(imgWeights, imgRef);
		VitimageUtils.adjustImageCalibration(imgFieldX, imgRef);
		VitimageUtils.adjustImageCalibration(imgFieldY, imgRef);
		VitimageUtils.adjustImageCalibration(imgFieldZ, imgRef);
		
		//Insert the needed informations
		imgWeights.getProcessor().set(0);
		imgFieldX.getProcessor().set(0);
		imgFieldY.getProcessor().set(0);
		imgFieldZ.getProcessor().set(0);
		
		for(int i=0;i<nPt;i++) {
			//System.out.println("Tentative d'un point "+vectPoints[i][0]+" , "+vectPoints[i][1]);
			if(   (vectPoints[i][2]+1>0 && vectPoints[i][2]+1<=dimensions[2]) &&
					(vectPoints[i][0]>=0 && vectPoints[i][0]<dimensions[0]) &&
					( vectPoints[i][1]>=0 &&  vectPoints[i][1]<dimensions[1]) ) {
				//System.out.println("Set");
				imgWeights.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1], 1);
				imgFieldX.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1], (float) vectVals[i][0]);
				imgFieldY.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1], (float) vectVals[i][1]);
				imgFieldZ.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1],(float) vectVals[i][2]);
			}
		}
		imgWeights=VitimageUtils.gaussianFilteringIJ(imgWeights, sigma,sigma , (zeroPaddingOutside ? 1 : 5)*sigma);//TODO : fix the zeroPadding stuff and set gaussian to ITK for performances
		imgFieldX=VitimageUtils.gaussianFilteringIJ(imgFieldX, sigma,sigma , (zeroPaddingOutside ? 1 : 5)*sigma);//TODO : the same for the function just after
//		imgFieldY.duplicate().show();
		imgFieldY=VitimageUtils.gaussianFilteringIJ(imgFieldY, sigma,sigma , (zeroPaddingOutside ? 1 : 5)*sigma);
//		imgFieldY.duplicate().show();
		imgFieldZ=VitimageUtils.gaussianFilteringIJ(imgFieldZ, sigma,sigma , (zeroPaddingOutside ? 1 : 5)*sigma);
		
		//Divide values by the smooth weights
		for(int z=0;z<dimensions[2];z++) {
			float[] valsW=(float [])imgWeights.getStack().getProcessor(z+1).getPixels();
			float[] valsX=(float [])imgFieldX.getStack().getProcessor(z+1).getPixels();
			float[] valsY=(float [])imgFieldY.getStack().getProcessor(z+1).getPixels();
			float[] valsZ=(float [])imgFieldZ.getStack().getProcessor(z+1).getPixels();
			for(int x=0;x<dimensions[0];x++) {
				for(int y=0;y<dimensions[1];y++){
					int index=dimensions[0]*y+x;
					if(valsW[index]<epsilon)valsW[index]=valsX[index]=valsY[index]=valsZ[index]=0;
					else{
						valsX[index]/=valsW[index];
						valsY[index]/=valsW[index];
						valsZ[index]/=valsW[index];
						valsW[index]/=valsW[index];
					}
				}
			}			
		}

		if(zeroPaddingOutside) {
			//Creer un nouveau vecteur de modifs
			ArrayList<Point3d> pts0=new ArrayList<Point3d>();
			ArrayList<Point3d> pts1=new ArrayList<Point3d>();
			int nX=(int) Math.ceil(voxSizes[0]/(2*sigma)*dimensions[0]);
			int nY=(int) Math.ceil(voxSizes[1]/(2*sigma)*dimensions[1]);
			int nZ=(int) Math.ceil(voxSizes[2]/(5*sigma)*dimensions[2]);
			IJ.log("Zero padding : adding correspondance blocks : "+nX+" X "+nY+" X "+nZ+" , total="+(nX*nY*nZ));
			int hits=0;
			for(int i=0;i<nPt;i++) {
				pts0.add(correspondancePoints[0][i]);
				pts1.add(correspondancePoints[1][i]);				
				for(int ii=-2;ii<3;ii++) {
					for(int jj=-2;jj<3;jj++) {
						for(int kk=-2;kk<3;kk++) {
							Point3d pt0=new Point3d(correspondancePoints[0][i].x+ii*voxSizes[0], correspondancePoints[0][i].y+jj*voxSizes[1],correspondancePoints[0][i].z+kk*voxSizes[2]);
							Point3d pt1=new Point3d(correspondancePoints[1][i].x+ii*voxSizes[0], correspondancePoints[1][i].y+jj*voxSizes[1],correspondancePoints[1][i].z+kk*voxSizes[2]);
							pts0.add(pt0);
							pts1.add(pt1);	
						}
					}
				}
			}
			for(int z=0;z<nZ-1;z++) {
				int indZ=(int) (Math.round(z*5*sigma)/voxSizes[2]);
				float[] valsW=(float [])imgWeights.getStack().getProcessor(indZ+1).getPixels();
				for(int x=0;x<nX-1;x++) {
					int indX=(int) (Math.round(x*2*sigma)/voxSizes[0]);
					for(int y=0;y<nY-1;y++) {
						int indY=(int) (Math.round(y*2*sigma)/voxSizes[1]);
						if(valsW[dimensions[0]*indY+indX]<epsilon) {
							hits++;
							pts0.add(new Point3d(x*2*sigma,y*2*sigma,z*5*sigma));
							pts1.add(new Point3d(x*2*sigma,y*2*sigma,z*5*sigma));
						}
					}
				}
			}
			IJ.log("Summary. Total size = "+(nX*nY*nZ)+" , padding  = "+hits+" points");
			Point3d [][]newCorr=new Point3d[2][pts0.size()];
			for(int i=0;i<pts0.size();i++) {
				newCorr[0][i]=pts0.get(i);
				newCorr[1][i]=pts1.get(i);
			}
			return computeDenseFieldFromSparseCorrespondancePoints(newCorr,imgRef,sigma,false);
		}
	  	return ItkImagePlusInterface.convertImagePlusArrayToDisplacementField(new ImagePlus [] {imgFieldX,imgFieldY,imgFieldZ});
	}
	
	public static ItkTransform computeDenseFieldFromSparseCorrespondancePoints(Point3d[][]correspondancePoints,ImagePlus imgRef,double sigma) {
		return new ItkTransform(new DisplacementFieldTransform( computeDenseFieldFromSparseCorrespondancePoints(correspondancePoints,imgRef,sigma,false)));
	}
	
	
	public static ItkTransform generateRandomDenseField(ImagePlus imgRef, int frequency,double mean, double std) {
		int X=imgRef.getWidth();
		int Y=imgRef.getHeight();
		int Z=imgRef.getNSlices();
		double sigma=VitimageUtils.getVoxelSizes(imgRef)[0]/frequency*imgRef.getWidth();
		int frequencyZ=frequency<Z ? frequency : Z;
		Point3d[][]correspondancePoints=new Point3d[2][frequencyZ*frequency*frequency];
		Random rand=new Random();
		int[][]coordinates=new int[frequency*frequency*frequencyZ][3];
		double []valuesX=new double[frequencyZ*frequency*frequency];
		double []valuesY=new double[frequencyZ*frequency*frequency];
		double []valuesZ=new double[frequencyZ*frequency*frequency];
		for(int x=0;x<frequency;x++)for(int y=0;y<frequency;y++)for(int z=0;z<frequencyZ;z++) {
			coordinates[x*frequencyZ*frequency+y*frequencyZ+z]=new int[] {
					(int)Math.round(((x+0.5)*X*1.0)/frequency),
					(int)Math.round(((y+0.5)*Y*1.0)/frequency),
					(int)Math.round(((z+0.4999)*Z*1.0)/frequencyZ)
			};
		}
		for(int z=0;z<Z;z++) for(int x=0;x<frequency;x++)for(int y=0;y<frequency;y++) {
			valuesX[x*frequencyZ*frequency+y*frequencyZ+z]=rand.nextGaussian()*std+mean;
			valuesY[x*frequencyZ*frequency+y*frequencyZ+z]=rand.nextGaussian()*std+mean;
			valuesZ[x*frequencyZ*frequency+y*frequencyZ+z]=(Z<std || Z==1) ? 0 : (rand.nextGaussian()*std+mean);
		}
		for(int i=0;i<correspondancePoints[0].length;i++) {
			correspondancePoints[0][i]=new Point3d(coordinates[i][0],coordinates[i][1],coordinates[i][2]);
			correspondancePoints[1][i]=new Point3d(coordinates[i][0]+valuesX[i],coordinates[i][1]+valuesY[i],coordinates[i][2]+valuesZ[i]);
		}		
		return new ItkTransform(new DisplacementFieldTransform( computeDenseFieldFromSparseCorrespondancePoints(correspondancePoints, imgRef, sigma, false)   )  );
	}
	
	
	public ImagePlus distanceMap(ImagePlus imgRef,boolean propToImageSize){
		ImagePlus ret=imgRef.duplicate();
		IJ.run(ret,"32-bit","");
		int X=imgRef.getWidth();
		int Y=imgRef.getHeight();
		int Z=imgRef.getNSlices();
		double[]voxSizes=VitimageUtils.getVoxelSizes(imgRef);
		double vx=voxSizes[0];
		double vy=voxSizes[1];
		double vz=voxSizes[2];
		double imgSize=X*vx;
		for(int z=0;z<Z;z++) {
			float[]pix=(float[]) ret.getStack().getProcessor(z+1).getPixels();
			for(int x=0;x<X;x++)for(int y=0;y<Y;y++) {
				double xx=x*vx;
				double yy=y*vy;
				double zz=z*vz;
				double[]coordsTrans=this.transformPoint(new double[] {xx,yy,zz});
				double distance=VitimageUtils.distance(xx,yy,zz,coordsTrans[0],coordsTrans[1],coordsTrans[2]);
				if(propToImageSize)distance/=imgSize;
				pix[y*X+x]=(float) distance;
			}
		}
		return ret;
	}
	
	
	
	public double[]meanDistanceAfterTrans(ImagePlus imgRef,int nX,int nY,int nZ,boolean getPixelsDistance){
		int X=imgRef.getWidth();
		int Y=imgRef.getWidth();
		int Z=imgRef.getWidth();
		double[]voxSizes=VitimageUtils.getVoxelSizes(imgRef);
		double vx=voxSizes[0];
		double vy=voxSizes[1];
		double vz=voxSizes[2];
		int deltaX=X/nX;
		int deltaY=Y/nY;
		int deltaZ=Z/nZ;
		double[]tabData=new double[nX*nY*nZ];
		int incr=0;
		for(int x=0;x<nX;x++)for(int y=0;y<nY;y++)for(int z=0;z<nZ;z++) {
			double xx=x*vx*deltaX;
			double yy=y*vy*deltaY;
			double zz=z*vz*deltaZ;
			double[]coordsTrans=this.transformPoint(new double[] {xx,yy,zz});
			double distance=VitimageUtils.distance(xx,yy,zz,coordsTrans[0],coordsTrans[1],coordsTrans[2]);
			tabData[incr++]=distance;
		}
		return VitimageUtils.statistics1D(tabData);
	}
	
	
	public static ImagePlus smoothImageFromCorrespondences(int[][]coordinates,double[]values, ImagePlus imgRef,double sigma,boolean zeroPaddingOutside) {
		double epsilon = 10E-20;
		double []voxSizes=VitimageUtils.getVoxelSizes(imgRef);
		int []dimensions=VitimageUtils.getDimensions(imgRef);
		int nPt=values.length;

		ImagePlus imgWeights=new Duplicator().run(imgRef,1,1,1,imgRef.getNSlices(),1,1);
		IJ.run(imgWeights,"32-bit","");
		imgWeights=VitimageUtils.set32bitToValue(imgWeights, 0);
		ImagePlus imgFieldX=imgWeights.duplicate();
				
		for(int i=0;i<nPt;i++) {
			imgWeights.getStack().getProcessor(coordinates[i][2]+1).setf(coordinates[i][0], coordinates[i][1], 1);
			imgFieldX.getStack().getProcessor(coordinates[i][2]+1).setf(coordinates[i][0], coordinates[i][1], (float)values[i]);
		}
		
		imgWeights=VitimageUtils.gaussianFiltering(imgWeights, sigma,sigma ,dimensions[2]==1 ? 0 : sigma);
		imgFieldX=VitimageUtils.gaussianFiltering(imgFieldX, sigma,sigma , dimensions[2]==1 ? 0 : sigma);
		
		//Divide values by the smooth weights
		for(int z=0;z<dimensions[2];z++) {
			float[] valsW=(float [])imgWeights.getStack().getProcessor(z+1).getPixels();
			float[] valsX=(float [])imgFieldX.getStack().getProcessor(z+1).getPixels();
			for(int x=0;x<dimensions[0];x++) {
				for(int y=0;y<dimensions[1];y++){
					int index=dimensions[0]*y+x;
					if(valsW[index]<epsilon)valsW[index]=valsX[index]=0;
					else{
						valsX[index]/=valsW[index];
					}
				}
			}			
		}
		return imgFieldX;
	}
	
	
	
	
	
		
	public static Point3d[][]trimCorrespondances(Point3d[][] correspondancePoints,ImagePlus imgRef,double sigma,double rejectThreshold){
		IJ.log("Trim correspondances. Sigma  ="+sigma+" ="+sigma/imgRef.getCalibration().pixelWidth+" voxels");
		double epsilon = 10E-10;
		double epsilonRejection=10E-6;
		double []voxSizes=VitimageUtils.getVoxelSizes(imgRef);
		int []dimensions=VitimageUtils.getDimensions(imgRef);
		int nPt=correspondancePoints[0].length;
		int [][]vectPoints=new int[nPt][3];
		double [][]vectVals=new double[nPt][3];
		for(int i=0;i<vectPoints.length;i++) {
			vectPoints[i][0]=(int)Math.round(correspondancePoints[0][i].x/voxSizes[0]);
			vectPoints[i][1]=(int)Math.round(correspondancePoints[0][i].y/voxSizes[1]);
			vectPoints[i][2]=(int)Math.round(correspondancePoints[0][i].z/voxSizes[2]);
			vectVals[i][0]=correspondancePoints[1][i].x-correspondancePoints[0][i].x;
			vectVals[i][1]=correspondancePoints[1][i].y-correspondancePoints[0][i].y;
			vectVals[i][2]=correspondancePoints[1][i].z-correspondancePoints[0][i].z;
		}
		
		
		ImagePlus imgWeights=IJ.createImage("tempW", dimensions[0], dimensions[1], dimensions[2], 32);
		ImagePlus imgFieldX=IJ.createImage("tempX", dimensions[0], dimensions[1], dimensions[2], 32);
		ImagePlus imgFieldY=IJ.createImage("tempY", dimensions[0], dimensions[1], dimensions[2], 32);
		ImagePlus imgFieldZ=IJ.createImage("tempZ", dimensions[0], dimensions[1], dimensions[2], 32);
		VitimageUtils.adjustImageCalibration(imgWeights, imgRef);
		VitimageUtils.adjustImageCalibration(imgFieldX, imgRef);
		VitimageUtils.adjustImageCalibration(imgFieldY, imgRef);
		VitimageUtils.adjustImageCalibration(imgFieldZ, imgRef);
		
		imgWeights.getProcessor().set(0);
		imgFieldX.getProcessor().set(0);
		imgFieldY.getProcessor().set(0);
		imgFieldZ.getProcessor().set(0);
		
		for(int i=0;i<nPt;i++) {
			imgWeights.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1], 1);
			imgFieldX.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1], (float) vectVals[i][0]);
			imgFieldY.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1], (float) vectVals[i][1]);
			imgFieldZ.getStack().getProcessor(vectPoints[i][2]+1).setf(vectPoints[i][0], vectPoints[i][1],(float) vectVals[i][2]);
		}
		
		imgWeights=VitimageUtils.gaussianFiltering(imgWeights, sigma,sigma , sigma);
		imgFieldX=VitimageUtils.gaussianFiltering(imgFieldX, sigma,sigma , sigma);
		imgFieldY=VitimageUtils.gaussianFiltering(imgFieldY, sigma,sigma , sigma);
		imgFieldZ=VitimageUtils.gaussianFiltering(imgFieldZ, sigma,sigma , sigma);
		
		for(int z=0;z<dimensions[2];z++) {
			float[] valsW=(float [])imgWeights.getStack().getProcessor(z+1).getPixels();
			float[] valsX=(float [])imgFieldX.getStack().getProcessor(z+1).getPixels();
			float[] valsY=(float [])imgFieldY.getStack().getProcessor(z+1).getPixels();
			float[] valsZ=(float [])imgFieldZ.getStack().getProcessor(z+1).getPixels();
			for(int x=0;x<dimensions[0];x++) {
				for(int y=0;y<dimensions[1];y++){
					int index=dimensions[0]*y+x;
					if(valsW[index]<epsilon)valsX[index]=valsY[index]=valsZ[index]=0;
					else{
						valsX[index]/=valsW[index];
						valsY[index]/=valsW[index];
						valsZ[index]/=valsW[index];
					}
				}
			}			
		}
		int [] flagPoint=new int [nPt];
		int keepedPoints=0;
		for(int i=0;i<nPt;i++) {
			double []statsX=VitimageUtils.statistics1D(VitimageUtils.valuesOfImageAround(imgFieldX, vectPoints[i][0],  vectPoints[i][1],  vectPoints[i][2], sigma*40));
			double []statsY=VitimageUtils.statistics1D(VitimageUtils.valuesOfImageAround(imgFieldY, vectPoints[i][0],  vectPoints[i][1],  vectPoints[i][2], sigma*40));
			double []statsZ=VitimageUtils.statistics1D(VitimageUtils.valuesOfImageAround(imgFieldZ, vectPoints[i][0],  vectPoints[i][1],  vectPoints[i][2], sigma*40));
			if( (vectVals[i][0]>statsX[0]+rejectThreshold*statsX[1]+epsilonRejection || vectVals[i][0]<statsX[0]-rejectThreshold*statsX[1]-epsilonRejection ) ||
				(vectVals[i][1]>statsY[0]+rejectThreshold*statsY[1]+epsilonRejection || vectVals[i][1]<statsY[0]-rejectThreshold*statsY[1]-epsilonRejection ) ||
				(vectVals[i][2]>statsZ[0]+rejectThreshold*statsZ[1]+epsilonRejection || vectVals[i][2]<statsZ[0]-rejectThreshold*statsZ[1]-epsilonRejection ) ) {
				flagPoint [i]=-1;
			}
			else {
				flagPoint[i]=1;
				keepedPoints++;
			}
		}
		Point3d [][]newCorrespondances=new Point3d[2][keepedPoints];
		keepedPoints=0;
		for(int i=0;i<nPt;i++) {
			if(flagPoint[i]>0) {
				newCorrespondances[0][keepedPoints]=new Point3d(correspondancePoints[0][i].x,correspondancePoints[0][i].y,correspondancePoints[0][i].z);
				newCorrespondances[1][keepedPoints]=new Point3d(correspondancePoints[1][i].x,correspondancePoints[1][i].y,correspondancePoints[1][i].z);
				keepedPoints++;
			}
		}
		return newCorrespondances;
	}

	
	
	/*Transform images and points. Work recursively : level 0=split frames and channels if any, level1=split RGB if any, level2=process resulting 3D stacks*/
	//TODO : smoothingBeforeDownSampling.
	public ImagePlus transformImage(ImagePlus imgRefTemp, ImagePlus imgMov,boolean smoothingBeforeDownSampling) {
		return transformImage(imgRefTemp,imgMov,smoothingBeforeDownSampling,false,0,false);
	}
	
	public ImagePlus transformImage(ImagePlus imgRefTemp, ImagePlus imgMov) {
		return transformImage(imgRefTemp,imgMov,false);
	}
	
	public ImagePlus transformImageExtensive(ImagePlus imgRefTemp, ImagePlus imgMov,boolean smoothingBeforeDownSampling) {
		return transformImage(imgRefTemp,imgMov,smoothingBeforeDownSampling,false,0,true);
	}
	
	public ImagePlus transformImageExtensive(ImagePlus imgRefTemp, ImagePlus imgMov) {
		return transformImageExtensive(imgRefTemp,imgMov,false);
	}
	
	/*Transform images and points. Work recursively : level 0=split frames and channels if any, level1=split RGB if any, level2=process resulting 3D stacks*/
	//TODO : smoothingBeforeDownSampling.
	public ImagePlus transformImage(ImagePlus imgRefTemp, ImagePlus imgMov,boolean smoothingBeforeDownSampling,boolean timeActions, long initialTime,boolean extensive) {
		ImagePlus imgRef=null;
		if(imgRefTemp.getNChannels()==1 && imgRefTemp.getNFrames()==1)imgRef=imgRefTemp;
		else imgRef=new Duplicator().run(imgRefTemp, 1, 1, 1, imgRefTemp.getNSlices(), 1, 1);

		double minRange=imgMov.getDisplayRangeMin();
		double maxRange=imgMov.getDisplayRangeMax();
		if(imgMov.getNChannels()>1 || imgMov.getNFrames()>1) {
			if(timeActions)IJ.log("...Timing (HPM at start) : "+VitimageUtils.dou((System.currentTimeMillis()-initialTime)/1000.0)+" s");
			int nbZ=imgRef.getNSlices();
			int nbT=imgMov.getNFrames();
			int nbC=imgMov.getNChannels();
			IJ.log("Transformation of hyperstack nC="+nbC+", nbZ="+nbZ+", nbT="+nbT);
			ImagePlus []imgTabMov=VitimageUtils.stacksFromHyperstackFastBis(imgMov);
			if(timeActions)IJ.log("...Timing (HPM after hyperunstacking) : "+VitimageUtils.dou((System.currentTimeMillis()-initialTime)/1000.0)+" s");
			ImagePlus mult=null;
			//Si pas extensif, pas de jacobien.
				//Si pas dense, c'est pas long. On envoie.
				//Mais si dense, c est long quand meme. Alors on flatten.
			//Si extensif, jacobien. 
				//Si pas dense, c'est pas long. On envoie.
				//Mais si dense, on flatten
			
			ItkTransform trTemp=null;
			if(!isDense) {
				if(extensive) {				
					mult=ItkTransform.getJacobian(this,imgRef,60);
					double value2=VitimageUtils.getVoxelVolume(imgRef)/VitimageUtils.getVoxelVolume(imgMov);
					mult=VitimageUtils.makeOperationOnOneImage(mult, 2, value2, false);
				}
				trTemp=this;
			}
			else {
				Image itkImg=this.getFlattenDenseFieldAsDisplacementFieldImage(imgRef);
				if(extensive) {				
					mult=ItkTransform.getJacobianOfDisplacementField(itkImg,imgRef,60);
					double value2=VitimageUtils.getVoxelVolume(imgRef)/VitimageUtils.getVoxelVolume(imgMov);
					mult=VitimageUtils.makeOperationOnOneImage(mult, 2, value2, false);
				}
				trTemp=new ItkTransform(new DisplacementFieldTransform(itkImg));
			}
				
			if(extensive) {				
				mult=ItkTransform.getJacobian(trTemp,imgRef,60);
				double value2=VitimageUtils.getVoxelVolume(imgRef)/VitimageUtils.getVoxelVolume(imgMov);
				mult=VitimageUtils.makeOperationOnOneImage(mult, 2, value2, false);
			}
			for(int i=0;i<imgTabMov.length;i++) {
				imgTabMov[i]= trTemp.transformImage(imgRef, imgTabMov[i],smoothingBeforeDownSampling,timeActions,initialTime,false);
				String lab=imgTabMov[i].getStack().getSliceLabel(1);
				if(extensive && (lab != null) && (lab.contains("M0MAP") || lab.contains("T1SEQ") || lab.contains("T2SEQ") ||  lab.contains("T1T2SEQ") || lab.contains("EXTENSIVE"))) {
					int type=imgTabMov[i].getType();
					imgTabMov[i]=VitimageUtils.makeOperationBetweenTwoImages(imgTabMov[i],mult,2,true);
					imgTabMov[i]=VitimageUtils.restoreType(imgTabMov[i],type);
				}
				if(timeActions)IJ.log("...Timing (HPM after transforming stack "+i+"/"+imgTabMov.length+") : "+VitimageUtils.dou((System.currentTimeMillis()-initialTime)/1000.0)+" s");
				IJ.log("Transforming index "+i+"/"+imgTabMov.length + " : "+VitimageUtils.imageResume(imgTabMov[i]));
			}
			Concatenator con=new Concatenator();
			con.setIm5D(true);
			ImagePlus img=con.concatenate(imgTabMov,false);
			if(timeActions)IJ.log("...Timing (HPM after concatenating) : "+VitimageUtils.dou((System.currentTimeMillis()-initialTime)/1000.0)+" s");
			IJ.log("Hyperstack characteristics before hyperstacking : "+VitimageUtils.imageResume(img));
			img=HyperStackConverter.toHyperStack(img, nbC, nbZ,nbT,"xyztc","Grayscale");
			if(timeActions)IJ.log("...Timing (HPM after reordering) : "+VitimageUtils.dou((System.currentTimeMillis()-initialTime)/1000.0)+" s");
			VitimageUtils.adjustImageCalibration(img, imgRef);
			return img;
		}
		if(imgMov.getType()==4) {
			ImagePlus[] channels = ChannelSplitter.split(imgMov);
			for(int i=0;i<3;i++) {
				VitimageUtils.adjustImageCalibration(channels[i], imgMov);
				for(int z=1;z<=imgMov.getNSlices();z++)channels[i].getStack().setSliceLabel(imgMov.getStack().getSliceLabel(z), z);
				channels[i]=transformImage(imgRef,channels[i],smoothingBeforeDownSampling,timeActions,initialTime,extensive);
			}
			ImagePlus ret=new ImagePlus("",RGBStackMerge.mergeStacks(channels[0].getStack(),channels[1].getStack(),channels[2].getStack(),true));
			for(int z=1;z<=ret.getNSlices();z++)ret.getStack().setSliceLabel(channels[0].getStack().getSliceLabel(z), z);
			VitimageUtils.adjustImageCalibration(ret, imgRef);
			return ret;
		}
		double valMean=imgMov.getStack().getVoxel(0, 0, 0);
		//double valMean=VitimageUtils.minOfImage(new Duplicator().run(imgMov, imgMov.getNSlices()/2+1,imgMov.getNSlices()/2+1));
//		LUT lut=imgMov.getLuts()[0];
		ResampleImageFilter resampler=new ResampleImageFilter();
		resampler.setReferenceImage(ItkImagePlusInterface.imagePlusToItkImage(imgRef));
		resampler.setDefaultPixelValue(valMean);
		resampler.setTransform(this);
		ImagePlus img=ItkImagePlusInterface.itkImageToImagePlus(resampler.execute(ItkImagePlusInterface.imagePlusToItkImage(imgMov)));		

		VitimageUtils.adjustImageCalibration(img, imgRef);
		img.setDisplayRange(minRange, maxRange);
		int Zout=img.getNSlices();
		int Zin=imgMov.getNSlices();
		double[]coords=ItkTransform.getImageCenter(img);
		double[]voxs=VitimageUtils.getVoxelSizes(img);
		for(int z=1;z<=Zout;z++) {
			coords[2]=z*voxs[2];
			double []coordsTrans=this.transformPoint(coords);
			int zFin=(int) Math.round(coordsTrans[2]/voxs[2]);
			zFin=Math.max(1, Math.min(zFin, Zin));
			img.getStack().setSliceLabel(imgMov.getStack().getSliceLabel(zFin),z);
		}

		
		String lab=img.getStack().getSliceLabel(1);
		if(extensive && (lab != null) && (lab.contains("M0MAP") || lab.contains("T1SEQ") || lab.contains("T2SEQ") ||  lab.contains("T1T2SEQ") || lab.contains("EXTENSIVE")) ){
 			ImagePlus mult=ItkTransform.getJacobian(this,imgRef,40);
			double value2=VitimageUtils.getVoxelVolume(imgRef)/VitimageUtils.getVoxelVolume(imgMov);
			mult=VitimageUtils.makeOperationOnOneImage(mult, 2, value2, false);
			img=VitimageUtils.makeOperationBetweenTwoImages(img,mult,2,true);
		}
		//		img.setLut(lut);
		return img;
	}	
	
	public ImagePlus transformImage(int[]targetDims,double[]targetVoxs, ImagePlus imgMov,boolean smoothingBeforeDownSampling) {
		String unit=imgMov.getCalibration().getUnit();
		ImagePlus ref=ij.gui.NewImage.createImage("Ref",targetDims[0],targetDims[1],targetDims[2],imgMov.getBitDepth(),ij.gui.NewImage.FILL_BLACK);	
		VitimageUtils.adjustImageCalibration(ref,targetVoxs, unit);
		return transformImage(ref,imgMov,smoothingBeforeDownSampling);
	}	

	
	public ImagePlus transformImageExtensive(int[]targetDims,double[]targetVoxs, ImagePlus imgMov,boolean smoothingBeforeDownSampling) {
		String unit=imgMov.getCalibration().getUnit();
		ImagePlus ref=ij.gui.NewImage.createImage("Ref",targetDims[0],targetDims[1],targetDims[2],imgMov.getBitDepth(),ij.gui.NewImage.FILL_BLACK);	
		VitimageUtils.adjustImageCalibration(ref,targetVoxs, unit);
		return transformImageExtensive(ref,imgMov);
	}	

	
	public static ImagePlus resampleImage(int[]targetDims,double[]targetVoxs, ImagePlus imgMov,boolean smoothingBeforeDownSampling) {
		return (new ItkTransform()).transformImage(targetDims,targetVoxs,imgMov,smoothingBeforeDownSampling);
	}	
	
	public ImagePlus transformImageSegmentationByte(ImagePlus imgRef, ImagePlus imgMov,int min, int max) {
		ImagePlus[]threshTab=new ImagePlus[max-min+1];
		ImagePlus mov8=new Duplicator().run(imgMov);
		mov8.setDisplayRange(0, 255);
		IJ.run(mov8,"8-bit","");
		for(int thr=min;thr<=max;thr++) {
			threshTab[thr-min]=VitimageUtils.thresholdByteImage(mov8, thr, thr+1);
			IJ.run(threshTab[thr-min],"32-bit","");			
			int val=Math.min(  10    ,    Math.min(   threshTab[thr-min].getWidth()/20    ,   threshTab[thr-min].getHeight()/20  ));
			int valMean=(int)Math.round(      VitimageUtils.meanValueofImageAround(threshTab[thr-min],val,val,0,val)*0.5 + VitimageUtils.meanValueofImageAround(threshTab[thr-min],threshTab[thr-min].getWidth()-val-1,threshTab[thr-min].getHeight()-val-1,0,val)*0.5    );
			ResampleImageFilter resampler=new ResampleImageFilter();
			resampler.setDefaultPixelValue(valMean);
			resampler.setReferenceImage(ItkImagePlusInterface.imagePlusToItkImage(imgRef));
			resampler.setTransform(this);
			threshTab[thr-min]=ItkImagePlusInterface.itkImageToImagePlus(resampler.execute(ItkImagePlusInterface.imagePlusToItkImage(threshTab[thr-min])));
		}

		ImagePlus ret=new Duplicator().run(imgRef);
		VitimageUtils.adjustImageCalibration(ret, imgRef);
		IJ.run(ret,"8-bit","");
		float valMax=0;
		float val=0;
		int indMax=0;
		float[][][] in=new float[max-min+1][ret.getStackSize()][];
		byte[][] out=new byte[ret.getStackSize()][];
		int X=ret.getWidth();
		int Y=ret.getHeight();
		int Z=ret.getStackSize();
		for(int z=0;z<Z;z++) {
			for(int thr=min;thr<=max;thr++)in[thr-min][z]=(float []) threshTab[thr-min].getStack().getProcessor(z+1).getPixels();
			out[z]=(byte []) ret.getStack().getProcessor(z+1).getPixels();
			for(int x=0;x<X;x++) {
				for(int y=0;y<Y;y++) {
					valMax=-1;
					indMax=-1;
					for(int thr=min;thr<=max;thr++) {
						val=(float)(in[thr-min][z][y*X+x]);
						if(val>valMax) {valMax=val;indMax=thr;}
					}
					out[z][y*X+x]=(  ((byte) (indMax & 0xff)) );
				}			 
			}
		}
		return ret;
	}

	public static ImagePlus resampleImageReech(ImagePlus imgRef, ImagePlus imgMov) {
		int val=Math.min(  10    ,    Math.min(   imgMov.getWidth()/20    ,   imgMov.getHeight()/20  ));
		int valMean=(int)Math.round(      VitimageUtils.meanValueofImageAround(imgMov,val,val,0,val)*0.5 + VitimageUtils.meanValueofImageAround(imgMov,imgMov.getWidth()-val-1,imgMov.getHeight()-val-1,0,val)*0.5    );
		ResampleImageFilter resampler=new ResampleImageFilter();
		resampler.setDefaultPixelValue(valMean);
		resampler.setReferenceImage(ItkImagePlusInterface.imagePlusToItkImage(imgRef));
		double[]voxSRef=VitimageUtils.getVoxelSizes(imgRef);
		double[]voxSMov=VitimageUtils.getVoxelSizes(imgMov);
		ItkTransform tr=getTransformForResampling(voxSRef,voxSMov);
		resampler.setTransform(tr);
		return (ItkImagePlusInterface.itkImageToImagePlus(resampler.execute(ItkImagePlusInterface.imagePlusToItkImage(imgMov))));
	}	
	

	public Point3d transformPoint(Point3d pt) {
		VectorDouble vect=new VectorDouble(3);
		vect.set(0,pt.x);
		vect.set(1,pt.y);
		vect.set(2,pt.z);
		double []coords=ItkImagePlusInterface.vectorDoubleToDoubleArray(this.transformPoint(vect));
		return new Point3d(coords[0],coords[1],coords[2]);
	}

	public double[] transformPoint(double[]coords) {
		VectorDouble vect=new VectorDouble(3);
		vect.set(0,coords[0]);
		vect.set(1,coords[1]);
		vect.set(2,coords[2]);
		double []coordsOut=ItkImagePlusInterface.vectorDoubleToDoubleArray(this.transformPoint(vect));
		return coordsOut;
	}

	
	public Point3d transformPointInverse(Point3d pt) {
		VectorDouble vect=new VectorDouble(3);
		vect.set(0,pt.x);
		vect.set(1,pt.y);
		vect.set(2,pt.z);
		double []coords=ItkImagePlusInterface.vectorDoubleToDoubleArray(this.getInverse().transformPoint(vect));
		return new Point3d(coords[0],coords[1],coords[2]);
	}

	
	
	
	
	
	
	
	
	/* Visualize transform as images*/
	public ImagePlus viewAsGrid3D(ImagePlus imgRef,int pixelSpacing) {
		ImagePlus grid=VitimageUtils.getBinaryGrid(imgRef, pixelSpacing);
		return this.transformImage(imgRef,grid,false);
	}
	
	public ImagePlus[] showAsCoordinates(String title,int slice) {
		ImagePlus[]coordinates=ItkImagePlusInterface.convertItkTransformToImagePlusArray(this);
		coordinates[0].setTitle(title+".X");
		coordinates[1].setTitle(title+".Y");
		coordinates[2].setTitle(title+".Z");
		for(int i =0;i<3;i++) {
			coordinates[i].show();
			coordinates[i].resetDisplayRange();
			coordinates[i].getWindow().setSize(512, 512);
			coordinates[i].getCanvas().fitToWindow();
			coordinates[i].setSlice(slice);
			IJ.run(coordinates[i],"Fire","");
		}
		return coordinates;
	}
		
	public void showAsGrid3D(ImagePlus imgRef2,int pixelSpacing,String title,int slice) {
		ImagePlus imgRef=VitimageUtils.imageCopy(imgRef2);
		IJ.run(imgRef,"8-bit","");
		ImagePlus gridXY=VitimageUtils.getBinaryGrid(imgRef, pixelSpacing);
		ImagePlus tempXY=this.transformImage(imgRef,gridXY,false);
		tempXY.setTitle(title+"-XY plane");
		tempXY.show();
		tempXY.getWindow().setSize(512, 512);
		tempXY.getCanvas().fitToWindow();
		tempXY.setSlice(slice);

		ImagePlus imgRefXZ=VitimageUtils.switchAxis(imgRef, 2);
		ImagePlus gridXZ=VitimageUtils.getBinaryGrid(imgRefXZ, pixelSpacing);
		gridXZ=VitimageUtils.switchAxis(gridXZ, 2);
		ImagePlus tempXZ=this.transformImage(imgRef,gridXZ,false);
		tempXZ=VitimageUtils.switchAxis(tempXZ, 2);
		tempXZ.show();
		tempXZ.setTitle(title+"-XZ plane");
		tempXZ.getWindow().setSize(512, 512);
		tempXZ.getCanvas().fitToWindow();
		tempXZ.setSlice(slice);

		ImagePlus imgRefYZ=VitimageUtils.switchAxis(imgRef, 1);
		ImagePlus gridYZ=VitimageUtils.getBinaryGrid(imgRefYZ, pixelSpacing);
		gridYZ=VitimageUtils.switchAxis(gridYZ, 1);
		ImagePlus tempYZ=this.transformImage(imgRef,gridYZ,false);
		tempYZ=VitimageUtils.switchAxis(tempYZ, 1);
		tempYZ.show();
		tempYZ.setTitle(title+"-YZ plane");
		tempYZ.getWindow().setSize(512, 512);
		tempYZ.getCanvas().fitToWindow();
		tempYZ.setSlice(slice);

	}
	
	public static ImagePlus getJacobian(ItkTransform tr2,ImagePlus imgRef,int percentageThreshold) {
		if(tr2.isDense) {
			return getJacobianOfDisplacementField(tr2.getFlattenDenseFieldAsDisplacementFieldImage(imgRef), imgRef,percentageThreshold);
		}
		else {
			ItkTransform tr=tr2.simplify();
			double det=ItkTransform.itkTransformToIj3dTransform(tr).determinant();
			ImagePlus ret=VitimageUtils.setImageToValue(imgRef, det);
			return ret;
		}
	}
	
	public static ImagePlus getJacobianOfDisplacementField(Image df,ImagePlus imgRef,int percentageThreshold) {
		ImagePlus jac=ItkTransform.getJacobian(df,percentageThreshold);
		return VitimageUtils.clipFloatImage(jac, 1-percentageThreshold/100.0,1+percentageThreshold/100.0);
	}
	
	
	public static ImagePlus getJacobian(Image denseField,int percentageThreshold) {
		DisplacementFieldJacobianDeterminantFilter df=new  DisplacementFieldJacobianDeterminantFilter();
		@SuppressWarnings("unused")
		ImagePlus result= ItkImagePlusInterface.itkImageToImagePlus(df.execute(denseField));
		return VitimageUtils.clipFloatImage(result, 1-percentageThreshold/100.0,1+percentageThreshold/100.0);
	}

	
	
	
	
	
	
	
	
	
	
	
	
	/*Mathematical, geometrical and composition operations over transforms*/
	public ImagePlus normOfDenseField(ImagePlus imgRef) {
		//Recuperer les dimensions
		int dimX=imgRef.getWidth();
		int dimY=imgRef.getHeight();
		int dimZ=imgRef.getNSlices();
		
		//Construire les futures images hotes pour les dimensions x y et z
		ImagePlus ret;
		double []voxSizes=new double [] {imgRef.getCalibration().pixelWidth , imgRef.getCalibration().pixelHeight, imgRef.getCalibration().pixelDepth};
		ret=IJ.createImage("", dimX, dimY, dimZ, 32);
		ret.getCalibration().setUnit("mm");
		ret.getCalibration().pixelWidth=voxSizes[0];
		ret.getCalibration().pixelHeight=voxSizes[1];
		ret.getCalibration().pixelDepth=voxSizes[2];
	
		
		//Pour chaque voxel, calculer la transformee
		VectorDouble coords=new VectorDouble(3);
		double distance=0;
		VectorDouble coordsTrans=new VectorDouble(3);
		for(int k=0;k<dimZ;k++) {
			IJ.log(" "+((k*100)/dimZ)+" %");
			float[]tab=(float[])ret.getStack().getProcessor(k+1).getPixels();
			
			for(int i=0;i<dimX;i++)for(int j=0;j<dimY;j++) {
				int ind=dimX*j+i;
				coords.set(0,i*voxSizes[0]);
				coords.set(1,j*voxSizes[1]);
				coords.set(2,k*voxSizes[2]);
				coordsTrans=(this.transformPoint(coords));
				distance=Math.sqrt(  (coordsTrans.get(0)-coords.get(0)) * (coordsTrans.get(0)-coords.get(0)) + (coordsTrans.get(1)-coords.get(1)) * (coordsTrans.get(1)-coords.get(1)) + (coordsTrans.get(2)-coords.get(2)) * (coordsTrans.get(2)-coords.get(2)) );
				tab[ind]=(float)(distance);
			}
		}
		ret.resetDisplayRange();
		return ret;
	}
	
	public ItkTransform getFlattenDenseField(ImagePlus imgRef) {
		return new ItkTransform(new DisplacementFieldTransform(getFlattenDenseFieldAsDisplacementFieldImage(imgRef)));
	}
	
	public Image getFlattenDenseFieldAsDisplacementFieldImage(ImagePlus imgRef) {
		if(!this.isDense) {IJ.showMessage("Trying to flatten non dense transform");System.exit(0);}
		IJ.log("Flattening dense field transform with a geometry of "+TransformUtils.stringVector(VitimageUtils.getDimensions(imgRef), ""));
		VitimageUtils.printImageResume(imgRef);
		//Recuperer les dimensions
		int dimX=imgRef.getWidth();
		int dimY=imgRef.getHeight();
		int dimZ=imgRef.getNSlices();
		
		//Construire les futures images hotes pour les dimensions x y et z
		ImagePlus []ret=new ImagePlus[3];
		double []voxSizes=new double [] {imgRef.getCalibration().pixelWidth , imgRef.getCalibration().pixelHeight, imgRef.getCalibration().pixelDepth};
		for(int i=0;i<3;i++) {
			ret[i]=IJ.createImage("", dimX, dimY, dimZ, 32);
			ret[i].getCalibration().setUnit("mm");
			ret[i].getCalibration().pixelWidth=voxSizes[0];
			ret[i].getCalibration().pixelHeight=voxSizes[1];
			ret[i].getCalibration().pixelDepth=voxSizes[2];
		}

		//Pour chaque voxel, calculer la transformee
		VectorDouble coords=new VectorDouble(3);
		VectorDouble coordsTrans=new VectorDouble(3);
		for(int k=0;k<dimZ;k++) {
			if(dimZ>200 && k%20==0)IJ.log("Flattening vector field, processing slice "+k+"/"+dimZ);
			if(dimZ<200 && dimZ>50 && k%10==0)IJ.log("Flattening vector field, processing slice "+k+"/"+dimZ);
			if(dimZ<50 && dimZ>4 && k%5==0)IJ.log("Flattening vector field, processing slice "+k+"/"+dimZ);
			if(dimZ<4)IJ.log("Flattening vector field, processing slice "+k+"/"+dimZ);
			float[]tabX=(float[])ret[0].getStack().getProcessor(k+1).getPixels();
			float[]tabY=(float[])ret[1].getStack().getProcessor(k+1).getPixels();
			float[]tabZ=(float[])ret[2].getStack().getProcessor(k+1).getPixels();
			
			for(int i=0;i<dimX;i++) {
				for(int j=0;j<dimY;j++) {
					int ind=dimX*j+i;
					coords.set(0,i*voxSizes[0]);
					coords.set(1,j*voxSizes[1]);
					coords.set(2,k*voxSizes[2]);
					coordsTrans=(this.transformPoint(coords));
					tabX[ind]=(float)(coordsTrans.get(0)-coords.get(0));
					tabY[ind]=(float)(coordsTrans.get(1)-coords.get(1));
					tabZ[ind]=(float)(coordsTrans.get(2)-coords.get(2));
				}
			}
		}
		Image im= ItkImagePlusInterface.convertImagePlusArrayToDisplacementField(ret);
		return im;
	}
	
	public ItkTransform simplify() {
		Transform3D transIj=new Transform3D(this.toAffineArrayMonolineRepresentation());
		return ItkTransform.ij3dTransformToItkTransform(transIj);		
	}
	
	public ItkTransform getInverseOfDenseField() {
		if(!this.isDense) {IJ.showMessage("Trying to get inverse of non dense transform");System.exit(0);}
		ImagePlus[]imgs=ItkImagePlusInterface.convertDisplacementFieldToImagePlusArrayAndNorm(new DisplacementFieldTransform((org.itk.simple.Transform)this).getDisplacementField() );
		ImagePlus[]imgsInv=new ImagePlus[3];
		imgsInv[0]=new Duplicator().run(imgs[0]);
		IJ.run(imgsInv[0],"Multiply...","value=0 stack");
		imgsInv[1]=new Duplicator().run(imgs[0]);
		imgsInv[2]=new Duplicator().run(imgs[1]);
		
		double []voxs=VitimageUtils.getVoxelSizes(imgs[0]);
		int [] dims=VitimageUtils.getDimensions(imgs[0]);
		double sigma=Math.max(voxs[1], voxs[2]);
		int nbVox=(dims[0])*(dims[1])*(dims[2]);
		int iter=0;
		//Generer les paires de points
		Point3d[][]correspondancePoints=new Point3d[2][nbVox];

		for(int x=0;x<dims[0];x++) {
			if(x%20==0)IJ.log(" "+x+"/"+dims[0]);
			for(int y=0;y<dims[1];y++) {
				for(int z=0;z<dims[2];z++) {
					double xx=x*voxs[0];
					double yy=y*voxs[1];
					double zz=z*voxs[2];
					double dx=(imgs[0].getStack().getProcessor(z+1).getf(x, y));
					double dy=(imgs[1].getStack().getProcessor(z+1).getf(x, y));
					double dz=(imgs[2].getStack().getProcessor(z+1).getf(x, y));
					correspondancePoints[0][iter]=new Point3d(xx+dx,yy+dy,zz+dz);
					correspondancePoints[1][iter]=new Point3d(xx,yy,zz);
					iter++;
				}
			}
		}

		//Calculer le champ correspondant		
		return new ItkTransform(new DisplacementFieldTransform( computeDenseFieldFromSparseCorrespondancePoints(correspondancePoints,imgs[0],sigma,false) ));
	}
	
	public ItkTransform multiplyDenseField(double factor) {
			if(!this.isDense) {IJ.showMessage("Trying to multiplyDenseField non dense transform");System.exit(0);}
			MultiplyImageFilter mul=new MultiplyImageFilter();
			VectorIndexSelectionCastImageFilter vectFilter=new VectorIndexSelectionCastImageFilter();
			ComposeImageFilter compFilter=new ComposeImageFilter();
			DisplacementFieldTransform df=new DisplacementFieldTransform((Transform)(this));
			vectFilter.setIndex(0);Image ix=vectFilter.execute(df.getDisplacementField());
			vectFilter.setIndex(1);Image iy=vectFilter.execute(df.getDisplacementField());
			vectFilter.setIndex(2);Image iz=vectFilter.execute(df.getDisplacementField());
			ix=mul.execute(factor, ix);
			iy=mul.execute(factor, iy);
			iz=mul.execute(factor, iz);
			return (new ItkTransform(new DisplacementFieldTransform( compFilter.execute(ix,iy,iz)  )));
	
	}
		
	public static ItkTransform smoothDeformationTransform(ItkTransform tr,double sigmaX,double sigmaY,double sigmaZ) {
		ImagePlus[]imgs=ItkImagePlusInterface.convertItkTransformToImagePlusArray(tr);
		for(int i=0;i<3;i++)imgs[i]=VitimageUtils.gaussianFiltering(imgs[i], sigmaX, sigmaY, sigmaZ);
		return new ItkTransform(new DisplacementFieldTransform(ItkImagePlusInterface.convertImagePlusArrayToDisplacementField(imgs)));
	}
		
	public ItkTransform addTransform(ItkTransform tr) {
		super.addTransform(tr);
		if(!this.isDense)this.isDense=tr.isDense;
		this.isFlattened=false;
		return this;
	}
	
	public ItkTransform addTransform(Transform tr) {
		super.addTransform(tr);
		if(!this.isDense)this.isDense=!tr.isLinear();
		this.isFlattened=false;
		return this;
	}

	
	
	
	
	
	
	
	
	
	/* File and String I/O functions*/
	public void writeMatrixTransformToFile(String path) {
		SimpleITK.writeTransform(this.simplify(),path);
	}
		
	public void writeToFileWithTypeDetection(String path,ImagePlus imgRef) {
		if(this.isDense) {
			this.writeAsDenseField(path, imgRef);
		}
		else this.writeMatrixTransformToFile(path);
	}
	
	public void writeAsDenseFieldWithITKExporter(String path){
		if(!this.isDense) {IJ.showMessage("Trying to write non dense transform");System.exit(0);}
		String shortPath = (path != null) ? path.substring(0,path.indexOf('.')) : "";
		ImageFileWriter imWri=new ImageFileWriter();
		imWri.execute((new DisplacementFieldTransform((Transform)(this))).getDisplacementField(),shortPath+".mhd",false);
	}
	
	public static ItkTransform readFromDenseFieldWithITKImporter(String path){
		ImageFileReader imRead=new ImageFileReader();
		imRead.setFileName(path);
		return new ItkTransform(new DisplacementFieldTransform( imRead.execute() ));
	}
		
	public void writeAsDenseField(String path,ImagePlus imgRef) {
		if(!this.isDense) {IJ.showMessage("Trying to write as dense field non dense transform");System.exit(0);}
		String shortPath = (path != null) ? path.substring(0,path.indexOf('.')) : "";
		ImagePlus[]trans=new ImagePlus[3];
		
		DisplacementFieldTransform df=new DisplacementFieldTransform((Transform)(this.getFlattenDenseField(imgRef)));
		trans=ItkImagePlusInterface.convertDisplacementFieldToImagePlusArrayAndNorm(df.getDisplacementField());
		IJ.saveAsTiff(trans[0],shortPath+".x.tif");
		IJ.saveAsTiff(trans[1],shortPath+".y.tif");
		IJ.saveAsTiff(trans[2],shortPath+".z.tif");
		IJ.run(trans[0],"8-bit","");
		IJ.saveAsTiff(trans[0],shortPath+".transform.tif");
	}
		
	public static ItkTransform readAsDenseField(String path) {
		
		if((path==null) || (! (path.substring(path.length()-14,path.length())).equals(".transform.tif"))) {
			IJ.log("Wrong file for dense field : "+path+" \n A dense field should be identified with an extension .transform.tif");
			return null;
		}
		
		String shortPath = path.substring(0,path.length()-14);
		ImagePlus[]trans=new ImagePlus[3];
		trans[0]=IJ.openImage(shortPath+".x.tif");
		trans[1]=IJ.openImage(shortPath+".y.tif");
		trans[2]=IJ.openImage(shortPath+".z.tif");
		return new ItkTransform(new DisplacementFieldTransform(ItkImagePlusInterface.convertImagePlusArrayToDisplacementField(trans)));
	}
	
	public static ItkTransform readTransformFromFile(String path) {
		ItkTransform tr=null;
		try{
			if(path.charAt(path.length()-1) == 'f') tr=readAsDenseField(path);
			else tr=new ItkTransform(SimpleITK.readTransform(path));
			return tr;
		} catch (Exception e) {		IJ.log("Wrong transform file or file selection was incompletely done in interface.\n Please select a   *.transform.tif file or a *.txt file");return null; }
	}

	public static String stringMatrix(String sTitre,double[]tab){
		//A reecrire au vu des decouvertes effectuees sur les chevrons
		//Ce sera la deuxieme passe
		String s=new String();
		s+=sTitre;
		s+="\n";		
		for(int i=0;i<3;i++){
			s+="[ ";
			for(int j=0;j<3;j++){
				s+=tab[i*4+j];
				s+=" , ";
			}
			s+=tab[i*4+3];
			s+=" ] \n";
		}
		s+= "[ 0 , 0 , 0 , 1 ]\n";
		return(s);	
	}

	public String drawableString() {
		double[][]array=this.toAffineArrayRepresentation();
		String str=String.format("[%8.5f  %8.5f  %8.5f  %8.5f]\n[%8.5f  %8.5f  %8.5f  %8.5f]\n[%8.5f  %8.5f  %8.5f  %8.5f]\n[%8.5f  %8.5f  %8.5f  %8.5f]",
									array[0][0] , array[0][1] , array[0][2] , array[0][3] ,
									array[1][0] , array[1][1] , array[1][2] , array[1][3] ,
									array[2][0] , array[2][1] , array[2][2] , array[2][3] ,
									array[3][0] , array[3][1] , array[3][2] , array[3][3] );
		return str;
	}

	public String toString(String title) {
		//A reecrire au vu des decouvertes effectuees sur les chevrons
		//Ce sera la deuxieme passe
		String ret="";
		int nb=this.nbTransformComposed();
		ret=this.toString();
		if(nb==1) {
			return("Transformation "+title+"\nDe type transformation ITK à "+nb+" composante\n>>>>>>>> Composante 1 >>>>>>>>>>>>>>>>>>>>>>>>\n"+(itkTransfoStepToString(ret.substring(ret.indexOf("\n")))));
		}
		else {
			String []tab1=ret.split("<<<<<<<<<<");
			String[] tabActives=(tab1[1].split("\n")[2]).split("[ ]{1,}");
			String[] transforms=tab1[0].split(">>>>>>>>>");
			ret="Transformation "+title+"\nDe type transformation ITK à "+nb+" composantes\n";
			for(int i=1;i<transforms.length;i++) {
				ret+=">>>>>>>> Composante "+i+" ("+(tabActives[i].equals("1") ? "libre" : "fixée")+
						") >>>>>>>>>>>>>>>>\n"+itkTransfoStepToString(transforms[i]) ;
			}
			return ret;
		}
	}

	
	
	
	
	
	
	public boolean isEqualToAffineTransform(ItkTransform tr2,double epsilonRotation,double epsilonTranslation) {
		double[][]array1=this.toAffineArrayRepresentation();
		double[][]array2=tr2.toAffineArrayRepresentation();
		
		for(int lin=0;lin<3;lin++)for(int col=0;col<3;col++)if(Math.abs(array1[lin][col]-array2[lin][col])>epsilonRotation)return false;
		for(int lin=0;lin<3;lin++)if(Math.abs(array1[lin][3]-array2[lin][3])>epsilonTranslation)return false;
		return true;
	}

	public boolean isIdentityAffineTransform(double epsilonRotation,double epsilonTranslation) {
		double[][]array=this.toAffineArrayRepresentation();
		
		for(int lin=0;lin<3;lin++)for(int col=0;col<3;col++) {
			if((lin==col) && (Math.abs(1-array[lin][col])>epsilonRotation))return false;
			if((lin!=col) && (Math.abs(array[lin][col])>epsilonRotation))return false;
		}
		for(int lin=0;lin<3;lin++)if(Math.abs(array[lin][3])>epsilonTranslation)return false;
		return true;
	}
	
	public String itkTransfoStepToString(String step){		 
		//A reecrire au vu des decouvertes effectuees sur les chevrons
		//Ce sera la deuxieme passe
		double[]mat= itkTransformStepToArray(step);
		String strType=(((step).split("\n"))[1]).split("[ ]{1,}")[1];
		if(strType.equals("Euler3DTransform")) {
			String angles=(((step).split("\n"))[21]).split(":")[1];
			strType+=angles;
		}
		return (stringMatrix("Categorie geometrique : "+strType,mat));
	}

	public double[] itkTransformStepToArray(String step) {
		//A reecrire au vu des decouvertes effectuees sur les chevrons
		//Ce sera la deuxieme passe
		String strInit=step;
		String []tabLign=strInit.split("\n");
		String detectIdentity=tabLign[1].split("[ ]{1,}")[1];
		if(detectIdentity.equals("IdentityTransform")) {
			return (new double[] {1,0,0,0,0,1,0,0,0,0,1,0});
		}
		else if(detectIdentity.equals("TranslationTransform")) {
			String valsTrans[]=tabLign[9].split("\\[")[1].split("\\]")[0].split(", ");
			return (new double[] {1,0,0,Double.valueOf(valsTrans[0]),0,1,0,Double.valueOf(valsTrans[1]),0,0,1,Double.valueOf(valsTrans[2])});
		}
		String []vals123=tabLign[10].split("[ ]{1,}");
		String []vals456=tabLign[11].split("[ ]{1,}");
		String []vals789=tabLign[12].split("[ ]{1,}");
		String []valsT=((((tabLign[13].split("\\[")[1]).split("\\]"))[0]).split(", "));
		return(new double[] {Double.parseDouble(vals123[1]),Double.parseDouble(vals123[2]),Double.parseDouble(vals123[3]),Double.parseDouble(valsT[0]),
				Double.parseDouble(vals456[1]),Double.parseDouble(vals456[2]),Double.parseDouble(vals456[3]),Double.parseDouble(valsT[1]),
				Double.parseDouble(vals789[1]),Double.parseDouble(vals789[2]),Double.parseDouble(vals789[3]),Double.parseDouble(valsT[2]) } );		
	}


	/*Others*/
	public int nbTransformComposed() {
		VitiDialogs.notYet("ItkTransform > nbTransformComposed");
		return 0;
	}

	public boolean isDense() {
		return this.isDense;
	}
	
	public static double estimateGlobalDilationFactor(Point3d[]setRef,Point3d[]setMov) {
		FastMatrix fm=FastMatrix.bestRigid( setMov, setRef, true );
		IJ.log("Similarity transform computed. Coefficient of dilation : "+Math.pow(fm.det(),0.333333));
		return Math.pow(fm.det(),0.333333);
	}
	

	
	
	public static void transformImageWithGui() {
		ImagePlus imgMov=VitiDialogs.chooseOneImageUI("Select the image to transform (moving image)","Select the image to transform (moving image)");
		ImageProcessor ip=imgMov.getStack().getProcessor(imgMov.getNSlices()/2+1);
		ip.resetMinAndMax();
		double rangeMin=ip.getMin();
		double rangeMax=ip.getMax();
		if(imgMov==null) {IJ.showMessage("Moving image does not exist. Abort.");return;}
		ImagePlus imgRef=VitiDialogs.chooseOneImageUI("Select the reference image, giving output dimensions (it can be the same)","Select the reference image, giving output dimensions (it can be the same)");
		ItkTransform tr=VitiDialogs.chooseOneTransformsUI("Select the transform to apply , .txt for Itk linear and .transform.tif for Itk dense", "", false);
		if(tr==null) {IJ.showMessage("No transform given in transformImageWithGui. Abort");return;}
		if(imgRef==null) {IJ.showMessage("No reference image provided. Moving image will be used as reference image.");imgRef=VitimageUtils.imageCopy(imgMov);}
		ImagePlus result=tr.transformImage(imgRef, imgMov, false);
		result.setTitle("Transformed image");
		result.setDisplayRange(rangeMin,rangeMax);
		result.show();
	}
	
	public static void composeTransformsWithGui() {
		ArrayList<ItkTransform> listTr=new ArrayList<ItkTransform>();
		boolean oneMore=true;
		int num=1;
		while(oneMore) {
			ItkTransform tr=VitiDialogs.chooseOneTransformsUI("Select the transform #"+(num++)+" , .txt for Itk linear and .transform.tif for Itk dense", "", false);
			if(tr==null) {tr=new ItkTransform();IJ.showMessage("Warning : you included a bad transform file. It was replaced by an identity transform\nin order the process is to be interrupted");}
			listTr.add(tr);
			oneMore=VitiDialogs.getYesNoUI("One more transform ?","One more transform ?");
		}
		ItkTransform trGlob=new ItkTransform();
		for(int i=0;i<listTr.size();i++)trGlob.addTransform(listTr.get(i));
		if(trGlob.isDense()) {
			ImagePlus imgRef=VitiDialogs.chooseOneImageUI("Select the reference image, giving output space dimensions","Select the reference image, giving output space dimensions");
			VitiDialogs.saveDenseFieldTransformUI(trGlob, "Save the resulting composed transform",false,"", "composed_transform.tif", imgRef);
		}
		else {
			VitiDialogs.saveMatrixTransformUI(trGlob, "Save the resulting composed transform", false, "", "composed_transform.txt");
		}
		IJ.showMessage("Transform successfully saved.");
	}

	

	
	public ImagePlus getJacobianHomeMadeBecauseOfUnavoidedCoreDumpIssueWithSimpleITKDisplacementFieldJacobianDeterminantFilter(ImagePlus imgRef,double sigma,int percentageThreshold) {
		if(!this.isDense) {IJ.showMessage("Trying to flatten non dense transform");System.exit(0);}
		IJ.log("Computing jacobian for a geometry of "+TransformUtils.stringVector(VitimageUtils.getDimensions(imgRef), ""));
		//Recuperer les dimensions
		int dimX=imgRef.getWidth();
		int dimY=imgRef.getHeight();
		int dimZ=imgRef.getNSlices();
		double[] dimsReal=VitimageUtils.getDimensionsRealSpace(imgRef);
		
		double []voxs=VitimageUtils.getVoxelSizes(imgRef);
		
		//stride in each dimension
		int deltaX=(int)Math.ceil(sigma/(2*voxs[0]));
		int deltaY=(int)Math.ceil(sigma/(2*voxs[1]));
		int deltaZ=(int)Math.ceil(sigma/(2*voxs[2]));
		int nX=dimX/deltaX;
		int nY=dimY/deltaY;
		int nZ=dimZ/deltaZ;
		int x,y,z,index;
		int nHits=nX*nY*nZ;
		System.out.println(nX+","+nY+","+nZ+","+nHits);
		int [][]coordinates=new int[nHits][3];
		double []values=new double[nHits];
		for(int zz=0;zz<nZ;zz++) {
			for(int xx=0;xx<nX;xx++) {
				for(int yy=0;yy<nY;yy++) {
					x=xx*deltaX;
					y=yy*deltaY;
					z=zz*deltaZ;
					index=xx + yy*nX + zz*nY*nX;
					double[]initOrigin=new double[] {x*voxs[0],y*voxs[1],z*voxs[2]};
					double[]initXPlus=new double[] {(x+sigma/2)*voxs[0],y*voxs[1],z*voxs[2]};
					double[]initYPlus=new double[] {(x)*voxs[0],(y+sigma/2)*voxs[1],z*voxs[2]};
					double[]initZPlus=new double[] {(x)*voxs[0],y*voxs[1],(z+sigma/2)*voxs[2]};
					
					double[]endOrigin=this.transformPoint(initOrigin);
					double[]vectEndXPlus=TransformUtils.vectorialSubstraction(this.transformPoint(initXPlus),endOrigin);
					double[]vectEndYPlus=TransformUtils.vectorialSubstraction(this.transformPoint(initYPlus),endOrigin);
					double[]vectEndZPlus=TransformUtils.vectorialSubstraction(this.transformPoint(initZPlus),endOrigin);
					
					double volInit=VitimageUtils.getVoxelVolume(imgRef)*sigma/2*sigma/2*sigma/2;
					double volFinal=TransformUtils.scalarProduct(vectEndZPlus,TransformUtils.vectorialProduct( vectEndXPlus, vectEndYPlus) );
					coordinates[index]=new int[] {x,y,z};
					values[index]=volFinal/volInit;
					if(values[index]<0)values[index]=-values[index];
				}
			}
		}
		
		ImagePlus img=smoothImageFromCorrespondences(coordinates,values, imgRef,sigma,false);
		return VitimageUtils.clipFloatImage(img, 1-percentageThreshold/100.0, 1+percentageThreshold/100.0);
	}
	



}
