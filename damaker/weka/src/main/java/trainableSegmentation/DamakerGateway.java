package trainableSegmentation;

import java.util.Arrays;

import ij.IJ;
import ij.process.*;
import ij.ImagePlus;
import ij.ImageStack;
import ij.gui.Roi;
import ij.process.ImageConverter;
import py4j.GatewayServer;

public class DamakerGateway {
	
	boolean[] enabledFeatures = new boolean[]{
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
	
	public static void main(String[] args) {		
		// DamakerGateway dg = new DamakerGateway();		
		// dg.start();
		
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
		
		
		new ij.ImageJ();
		Weka_Segmentation ws = new Weka_Segmentation();
		ws.run("");
		
	}
	
	GatewayServer gatewayServer;
	public DamakerGateway() {
		gatewayServer = new GatewayServer(this);
	}
	
	public void prl(byte[] l) {
		for (byte b : l) {
			System.out.println(b);
		}
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
		
		WekaSegmentation segmentator = new WekaSegmentation( input );
		segmentator.setEnabledFeatures(enabledFeatures);
		
		if (!segmentator.loadClassifier(modelpath))
			System.out.println("Weka - Could not load training model");
		
		segmentator.applyClassifier(false);
		ImagePlus classifiedImage = segmentator.getClassifiedImage();
		IJ.save(classifiedImage, outpath);
		segmentator.shutDownNow();
	}
	
	public void runSegmentation(ImagePlus img, String modelpath, String outpath) {		
		WekaSegmentation segmentator = new WekaSegmentation( img );
		segmentator.setEnabledFeatures(enabledFeatures);
		
		if (!segmentator.loadClassifier(modelpath))
			System.out.println("Weka - Could not load training model");
		
		segmentator.applyClassifier(false);
		ImagePlus classifiedImage = segmentator.getClassifiedImage();
		IJ.save(classifiedImage, outpath);
		segmentator.shutDownNow();
	}
	
	public ImagePlus numpyToImagePlus(byte[] px, int w, int h, int d) {
		ImageStack img_stack = new ImageStack(w, h);
		
		for (int i=0; i < d; i++) {
			img_stack.addSlice(null, Arrays.copyOfRange(px, i*w*h, (i+1)*w*h));
		}
		
		return new ImagePlus("", img_stack);
	}
	
	public void prObj(Object o) {
		System.out.println(o.getClass());
	}
}
