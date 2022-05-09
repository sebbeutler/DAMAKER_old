package fr.cirad.image.registration;

import java.util.Arrays;

import fr.cirad.image.fijiyama.RegistrationAction;
import ij.IJ;
import ij.process.*;
import ij.ImagePlus;
import ij.ImageStack;
import ij.gui.Roi;
import ij.process.ImageConverter;
import py4j.GatewayServer;

public class DamakerGateway {
	
	public static void main(String[] args) {		
		// DamakerGateway dg = new DamakerGateway();		
		// dg.start();
		ImagePlus ref = IJ.openImage("../../resources/registration/C1-E0.tif");
		ImagePlus mov = IJ.openImage("../../resources/registration/C1-E1.tif");
		
		RegistrationAction regAct = new RegistrationAction();
		
		
		BlockMatchingRegistration bmr = BlockMatchingRegistration.setupBlockMatchingRegistration(ref, mov, regAct);
		bmr.runBlockMatching(null, false);
		
	}
	
	GatewayServer gatewayServer;
	public DamakerGateway() {
		gatewayServer = new GatewayServer(this);
	}
	
	public void start() {
		gatewayServer.start();
		System.out.println("Py4J gateway started.");
	}
	
	public ImagePlus open(String filepath) {
		 return IJ.openImage( filepath );
	}
}
