import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int H,M;		
		H = sc.nextInt(); M = sc.nextInt();		
		
		if (M - 45 >= 0) {
			M = M - 45;
		}
		else if (M - 45 < 0) {
			if (H > 0) {
				H = H - 1;
				M = M + 15;
			}
			else if (H == 0) {
				H = 23;
				M = M + 15;
			}
		}		
		int a = H;
		int b = M;
		System.out.println(a+" "+b);		
	}
}
