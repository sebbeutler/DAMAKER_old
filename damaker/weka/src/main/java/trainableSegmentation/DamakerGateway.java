package trainableSegmentation;

import java.io.Console;
import java.util.Arrays;

import ij.IJ;
import ij.ImagePlus;
import ij.ImageStack;
import py4j.GatewayServer;
import weka.classifiers.AbstractClassifier;

public class DamakerGateway {
	
	public class CustomGateway extends GatewayServer {
		public CustomGateway(Object entry_point) {
			super(entry_point);
		}

		@Override
		public void shutdown() {
			super.shutdown();
			System.out.println("Py4J stopped.");
			System.exit(0);
		}
		
		@Override
		public void serverPostShutdown() {
			super.serverPostShutdown();
			System.out.println("Py4J post-stopped.");
			System.exit(0);
		}
	}
	
	boolean[] enabledFeatures2D = new boolean[]{
			false, 	/* Gaussian_blur */
			false, 	/* Sobel_filter */
			false, 	/* Hessian */
			false, 	/* Difference_of_gaussians */
			false, 	/* Membrane_projections */
			true, 	/* Variance */
			true, 	/* Mean */
			false, 	/* Minimum */
			false, 	/* Maximum */
			false, 	/* Median */
			false,	/* Anisotropic_diffusion */
			false, 	/* Bilateral */
			false, 	/* Lipschitz */
			false, 	/* Kuwahara */
			false,	/* Gabor */
			false, 	/* Derivatives */
			false, 	/* Laplacian */
			false,	/* Structure */
			false,	/* Entropy */
			false	/* Neighbors */
	};
	
	boolean[] enabledFeatures3D = new boolean[]{
			false, 	/* Gaussian_blur */
			false, 	/* Hessian */
			false, 	/* Derivatives */
			false, 	/* Laplacian */
			false,	/* Structure */
			false,	/* Edges */
			false,	/* Difference of Gaussian */
			false,	/* Minimum */
			false,	/* Maximum */
			true,	/* Mean */
			false,	/* Median */
			true	/* Variance */
	    };
	
	public static void main(String[] args) {		
		DamakerGateway dg = new DamakerGateway();		
		dg.start();
		/*
		WekaSegmentation segmentator = new WekaSegmentation(  IJ.openImage( "../../resources/segmentation/C1-E0.tif" ) );
		segmentator.setEnabledFeatures(dg.enabledFeatures);
		
		segmentator.addExample(0, new Roi(222, 31, 30, 20), 46);
		segmentator.addExample(1, new Roi(216, 80, 30, 20), 46);
		
		segmentator.addExample(0, new Roi(218, 9, 30, 20), 84);
		segmentator.addExample(1, new Roi(207, 71, 30, 20), 84);
		
		segmentator.addExample(0, new Roi(222, 21, 30, 20), 122);
		segmentator.addExample(1, new Roi(75, 27, 30, 20), 122);
		
		segmentator.trainClassifier();
		segmentator.applyClassifier(false);
		ImagePlus img = segmentator.getClassifiedImage();
		IJ.save(img, "out.tif");
		segmentator.shutDownNow();
		*/
		
		
		
		//IJ.save(img, "out.tif");
		
		/*
		new ij.ImageJ();
		Weka_Segmentation ws = new Weka_Segmentation();
		ws.run("");
		*/
		
	}
	
	GatewayServer gatewayServer;
	public DamakerGateway() {
		gatewayServer = new CustomGateway(this);

	}
	
	public void start() {
		gatewayServer.start();
		System.out.println("Py4J gateway started.");
	}
	
	public ImagePlus open(String filepath) {
		 return IJ.openImage( filepath );
	}	

	public void print(String arg) {
		System.out.println(arg);
	}
	
	
	public void runSegmentation(String filepath, String modelpath, String outpath) {
		ImagePlus input  = IJ.openImage( filepath );
		
		WekaSegmentation segmentator = new WekaSegmentation( true );
		segmentator.setEnabledFeatures(enabledFeatures3D);
		
		if (!segmentator.loadClassifier(modelpath)) {
			System.out.println("Weka - Could not load training model");
			return;
		}
		
		segmentator.loadNewImage(input);
		
		segmentator.applyClassifier(false);
		ImagePlus classifiedImage = segmentator.getClassifiedImage();
		IJ.save(classifiedImage, outpath);
		segmentator.shutDownNow();
	}
	
	public void runSegmentation(ImagePlus img, String modelpath, String outpath) {
		
		WekaSegmentation segmentator = new WekaSegmentation( img );
		segmentator.setEnabledFeatures(enabledFeatures3D);
		
		if (!segmentator.loadClassifier(modelpath)) {
			System.out.println("Weka - Could not load training model");
			return;
		}
		AbstractClassifier cl = segmentator.getClassifier();
		System.out.println(cl.getOptions());
		segmentator.applyClassifier(img, 0, false);
		ImagePlus classifiedImage = segmentator.getClassifiedImage();
		IJ.save(classifiedImage, outpath);
		segmentator.shutDownNow();
	}
	
	public byte[][] runSegmentation(ImagePlus img, String modelpath) {
		System.out.println("Segmentation");
		WekaSegmentation segmentator = new WekaSegmentation( true );
		segmentator.setEnabledFeatures(enabledFeatures3D);
		segmentator.setTrainingImage(img);
		
		if (!segmentator.loadClassifier(modelpath)) {
			System.out.println("Weka - Could not load training model");
			return null;
		}
		
		segmentator.applyClassifier(false);
		ImagePlus classifiedImage = segmentator.getClassifiedImage();

		segmentator.shutDownNow();
		return imagePlusToByteArray(classifiedImage);
	}
	
	public byte[][] imagePlusToByteArray(ImagePlus img) {
		Object[] arr = img.getStack().getImageArray();
		byte[][] b_arr = new byte[img.getStackSize()][img.getHeight() + img.getWidth()];
		
		int j=0;
		for (int i=0; i < arr.length; i++) {
			if (arr[i] != null) {
				b_arr[j] = (byte[]) arr[i];
				j++;
			}
		}
		return b_arr;
	}
	
	public ImagePlus numpyToImagePlus(byte[] px, int w, int h, int d) {
		ImageStack img_stack = new ImageStack(w, h);
		
		for (int i=0; i < d; i++) {
			img_stack.addSlice(null, Arrays.copyOfRange(px, i*w*h, (i+1)*w*h));
		}
		
		return new ImagePlus("", img_stack);
	}
}
