import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();	
		int n = t;
		int a = 1;
		for (int p = 0; p < t; p++) {
			for (int j = 0; j < n-1; j++) {
				System.out.print(" ");				
			}
			n--;
			for (int i = 0; i < a; i++) {
				System.out.print("*");
			}
			a++;
			System.out.println();
		}
	}
}
