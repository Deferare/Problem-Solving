import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int n = sc.nextInt(); int saveN = n; int plus = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < saveN-1; j++) {
				System.out.print(" ");
			}
			for (int j = 0; j < i+plus; j++) {
				System.out.print("*");
			}
			System.out.println();
			plus+=1;
			saveN--;
		}
	}
}
