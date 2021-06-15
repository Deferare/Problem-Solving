import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int n = sc.nextInt();
		int sum = 0; int check = 0; int turn = 0;
		while (true) {
			if (turn == 0) {
				sum += 5;
				check++;
			}		
			else if (turn == 1) {
				int checkNum = n - sum;
				if (sum > n || checkNum%2 != 0) {
					sum -= 5;
					check--;
				}
				else if (sum < n) {
					if (checkNum%2 == 0) {
						sum += 2;
						check++;
					}
				}				
			}
			if (sum == n) {
				System.out.print(check);
				break;
			}
			else if (sum > n) {
				turn=1;
			}
			if (check < 0) {
				System.out.print(-1);
				break;
			}
		}
	}
}
