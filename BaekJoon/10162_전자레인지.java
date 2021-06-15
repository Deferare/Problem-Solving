import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cookingTime = sc.nextInt();
		int a = 300; int b = 60; int c = 10;
		int checkA = 0; int checkB = 0; int checkC = 0;		
		while(true) {
			if (cookingTime >= a) {
				cookingTime -= a;
				checkA++;
			}
			else if (cookingTime >= b) {
				cookingTime -= b;
				checkB++;
			}
			else if (cookingTime >= c) {
				cookingTime -= c;
				checkC++;
			}
			if (cookingTime == 0) {
				System.out.printf("%d %d %d",checkA,checkB,checkC);
				break;
			}
			else if (cookingTime < 10) {
				System.out.print(-1);
				break;
			}
		}		
	}	
}
