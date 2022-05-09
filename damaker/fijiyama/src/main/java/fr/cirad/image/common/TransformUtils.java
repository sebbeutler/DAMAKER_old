package fr.cirad.image.common;

import fr.cirad.image.common.VitimageUtils;

import ij.ImagePlus;
//import imagescience.transform.Transform;
import math3d.Point3d;


public interface TransformUtils {
	public enum Geometry{
		REFERENCE,
		QUASI_REFERENCE,
		SWITCH_XY,
		SWITCH_XZ,
		SWITCH_YZ,
		MIRROR_X,
		MIRROR_Y,
		MIRROR_Z,
		UNKNOWN
	}
		
	
	
	public enum Misalignment{
		NONE,
		LIGHT_RIGID,
		GREAT_RIGID,
		LIGHT_SIMILARITY,
		STRONG_SIMILARITY,
		LIGHT_DEFORMATION,
		STRONG_DEFORMATION,		
		VOXEL_SCALE_FACTOR,
		UNKNOWN
	}
	

	
		
	
	
	/**
	 * Mathematic utilities
	 * @param img
	 * @param computeZaxisOnly
	 * @param cornersCoordinates
	 * @param ignoreUnattemptedDimensions
	 * @return
	 */
	public static double calculateAngle(double x, double y)
	{
	    double angle = Math.toDegrees(Math.atan2(y, x));
	    // Keep angle between 0 and 360
	    angle = angle + Math.ceil( -angle / 360 ) * 360;

	    return angle;
	}
	
	public static double diffTeta(double teta1,double teta2) {
		//120   130  -> -10
		//130   120  -> 10
		//30    330  -> 30  -30  -> 60 
		//330    30  -> -30  30  -> -60 
		if(Math.abs(teta1-teta2)>180) {
			if(teta1>teta2)return(teta1-360-teta2);
			if(teta2>teta1)return(teta1-(teta2-360));
		}
		else {
			return teta1-teta2;
		}
		return 0;
	}


	@SuppressWarnings("rawtypes")
	class VolumeComparator implements java.util.Comparator {
		   public int compare(Object o1, Object o2) {
		      return ((Double) ((Object[]) o1)[0]).compareTo((Double)((Object[]) o2)[0]);
		   }
		}
	
	@SuppressWarnings("rawtypes")
	class AngleComparator implements java.util.Comparator {
	   public int compare(Object o1, Object o2) {
	      return ((Double) ((Double[]) o1)[2]).compareTo((Double)((Double[]) o2)[2]);
	   }
	}
	
	public static double norm(double[]v){
		double tot=0;
		for(int i=0;i<v.length;i++)tot+=v[i]*v[i];
		return Math.sqrt(tot);
	}

	public static double[] normalize(double[]v){
		double[] ret=new double[v.length];
		double nrm=norm(v);
		for(int i=0;i<v.length;i++)ret[i]=v[i]/nrm;
		return ret;
	}

	public static double scalarProduct(double[]v1,double []v2){
		double tot=0;
		for(int i=0;i<v1.length;i++)tot+=v1[i]*v2[i];
		return tot;
	}

	public static double scalarProduct(Point3d v1,Point3d v2){
		return(v1.x*v2.x+v1.y*v2.y+v1.z*v2.z);
	}

	public static double [] sumVector(double[]v,double []v2){
		return vectorialAddition(v, v2);
	}

	public static double [] sumVector(double[]v,double []v2,double[]v3){
		return sumVector(v,sumVector(v2,v3));
	}

	
	public static double [] multiplyVector(double[]v,double []v2){
		double[] ret=new double[3];
		ret[0]=v[0]*v2[0];
		ret[1]=v[1]*v2[1];
		ret[2]=v[2]*v2[2];
		return ret;
	}

	public static double [] multiplyVector(double[]v,double factor){
		double[] ret=new double[3];
		ret[0]=v[0]*factor;
		ret[1]=v[1]*factor;
		ret[2]=v[2]*factor;
		return ret;
	}

	public static double[] vectorialProduct(double[]v1,double[]v2){
		double[] ret=new double[3];
		ret[0]=v1[1]*v2[2]-v1[2]*v2[1];		
		ret[1]=v1[2]*v2[0]-v1[0]*v2[2];		
		ret[2]=v1[0]*v2[1]-v1[1]*v2[0];		
		return ret;
	}

	public static double[] vectorialSubstraction(double[]v1,double[]v2){
		double[] ret=new double[v1.length];
		for(int i=0;i<v1.length;i++)ret[i]=v1[i]-v2[i];		
		return ret;
	}

	public static double[] vectorialAddition(double[]v1,double[]v2){
		double[] ret=new double[v1.length];
		for(int i=0;i<v1.length;i++)ret[i]=v1[i]+v2[i];		
		return ret;
	}


	public static double[] vectorialMean(double[]v1,double[]v2){
		double[] ret=new double[v1.length];
		for(int i=0;i<v1.length;i++)ret[i]=(v1[i]+v2[i])/2.0;		
		return ret;
	}

	
	public static double[] invertVector(double[]v1){
		double[] ret=new double[v1.length];
		for(int i=0;i<v1.length;i++)ret[i]=1/v1[i];		
		return ret;
	}

	public static double[] proj_u_of_v(double[]u,double[]v){
		double scal1=scalarProduct(u,v);
		double scal2=scalarProduct(u,u);
		return multiplyVector(u,scal1/scal2);
	}
	
	public static Point3d convertPointToRealSpace(Point3d p,ImagePlus img) {
		double alpha=0;//for itk
		return new Point3d((p.x+alpha)*img.getCalibration().pixelWidth , (p.y+alpha)*img.getCalibration().pixelHeight , (p.z+alpha)*img.getCalibration().pixelDepth);
	}

	public static Point3d convertPointToImageSpace(Point3d p,ImagePlus img) {
		double alpha=0;//for itk
		return new Point3d(p.x/img.getCalibration().pixelWidth-alpha, p.y/img.getCalibration().pixelHeight-alpha, p.z/img.getCalibration().pixelDepth-alpha);
	}

	public static double[] point3dToDoubleArray(Point3d p) {return new double[] {p.x,p.y,p.z};}
	
	public static Point3d doubleArrayToPoint3d(double[]d) {return new Point3d(d[0],d[1],d[2]);}
	

	/**
	 * IO Utilities for Vectors and Matrices
	 * @param vect
	 * @param vectNom
	 */
	static void printVector(double []vect,String vectNom){
		System.out.println(vectNom+" = [ "+vect[0]+" , "+vect[1]+" , "+vect[2]+" ]");
	}

	static String stringVectorN(double []vect,String vectNom){
		String str=vectNom+" = [ ";
		for(int i=0;i<vect.length;i++)str+=vect[i]+(i==vect.length-1 ? " ]" : " , ");
		return str;
	}

	static String stringVectorNDou(double []vect,String vectNom){
		String str=vectNom+" = [ ";
		for(int i=0;i<vect.length;i++)str+=VitimageUtils.dou(vect[i])+(i==vect.length-1 ? " ]" : " , ");
		return str;
	}

	static String stringVectorN(int []vect,String vectNom){
		String str=vectNom+" = [ ";
		for(int i=0;i<vect.length;i++)str+=vect[i]+(i==vect.length-1 ? " ]" : " , ");
		return str;
	}

	static String stringMatrixN(int [][]vect,String vectNom){
		String str=vectNom+" = [ \n";
		for(int i=0;i<vect.length;i++)str+=stringVectorN(vect[i],"Ligne "+i+"")+"\n";
		str+=" ]";
		return str;
	}

	
	public static String stringMatrixMN(String sTitre,double[][] confusionMatrix){
		String s=new String();
		s+=""+sTitre+" , matrice de taille "+confusionMatrix.length+" X "+confusionMatrix[0].length+"\n";
		for(int i=0;i<confusionMatrix.length;i++){
			s+="[ ";
			for(int j=0;j<confusionMatrix[i].length-1;j++){
				s+=VitimageUtils.dou(confusionMatrix[i][j]);
				s+=" , ";
			}
			s+=VitimageUtils.dou(confusionMatrix[i][confusionMatrix[i].length-1])+" ] \n";
		}
		return s;
	}	
	public static String stringMatrixMN(String sTitre,int[][] confusionMatrix){
		String s=new String();
		s+=""+sTitre+" , matrice de taille "+confusionMatrix.length+" X "+confusionMatrix[0].length+"\n";
		for(int i=0;i<confusionMatrix.length;i++){
			s+="[ ";
			for(int j=0;j<confusionMatrix[i].length-1;j++){
				s+=VitimageUtils.dou(confusionMatrix[i][j]);
				s+=" , ";
			}
			s+=VitimageUtils.dou(confusionMatrix[i][confusionMatrix[i].length-1])+" ] \n";
		}
		return s;
	}	

	
	public static String stringVector(double []vect,String vectNom){
		return(vectNom+" = [ "+vect[0]+" , "+vect[1]+" , "+vect[2]+" ]");
	}

	public static String stringVectorDou(double []vect,String vectNom){
		return(vectNom+" = [ "+VitimageUtils.dou(vect[0])+" , "+VitimageUtils.dou(vect[1])+" , "+VitimageUtils.dou(vect[2])+" ]");
	}

	public static String stringVectorDou(double []vect,String vectNom,int n){
		return(vectNom+" = [ "+VitimageUtils.dou(vect[0],n)+" , "+VitimageUtils.dou(vect[1],n)+" , "+VitimageUtils.dou(vect[2],n)+" ]");
	}

	public static String stringVector(int []vect,String vectNom){
		return(vectNom+" = [ "+vect[0]+" , "+vect[1]+" , "+vect[2]+" ]");
	}
	


	
}
