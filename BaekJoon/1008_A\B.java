import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a,b;
		a = sc.nextDouble();
		b = sc.nextDouble();
		if (a <= 9 && b <= 9) {
			double c = (double)(a/b);
			System.out.println(c);
		}		
	}
}
