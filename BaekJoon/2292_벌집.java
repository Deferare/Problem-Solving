import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a = 1;
		int aS = 1;
		int check = 1;
		int multiple = 1;			
		while(true) {			
			a = a + 6*multiple;		
			if (a >= n && n >= aS) {
				if (n > 1) check += 1;
				System.out.print(check);
				break;
			}else {
				check++;
				multiple++;
				aS = a;	
			}								
		}
	}
}
