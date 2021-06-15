import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); 
		int change = 1000-n; int check = 0;	

		while(change > 0) {
			if (change >= 500) {
				change = change - 500; check++;
			}
			else if (change >= 100) {
				change = change - 100; check++;
			}
			else if (change >= 50) {
				change = change - 50; check++;
			}	
			else if (change >= 10) {
				change = change - 10; check++;
			}	
			else if (change >= 5) {
				change = change - 5; check++;
			}	
			else if (change >= 1) {
				change = change - 1; check++;
			}	
		}
		System.out.println(check);
	}
}
