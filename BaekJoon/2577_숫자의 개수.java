import java.util.Scanner;
public class Main {
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);		
		int a = scan.nextInt();
		int b = scan.nextInt();
		int c = scan.nextInt();		
		int d = a*b*c;
		int[] array = new int[10];			
		while(d > 0) { 
			int i = d%10; 
			array[i]++; 
			d /= 10; 
		}		
		for(int i : array) {
			System.out.println(i);
		}
	}
}
