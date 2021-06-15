import java.util.Scanner;
public class Main {
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);	
		double[] arr = new double[scan.nextInt()];
		double max = 0;
		double newAvg = 0;
		for (int i = 0; i < arr.length; i++) {
			arr[i] = scan.nextInt(); //점수 입력
			if (arr[i] > max) max = arr[i];
		}
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (arr[i]/max)*100; 	
			newAvg = newAvg + arr[i];
		}
		System.out.println(newAvg/arr.length);		
	}
}
