import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); int k = sc.nextInt(); int check = 0; int sum = 0; int k_clone = k;
		int[] coin = new int[n];
		for (int i = 0; i < n; i++) {
			coin[i] = sc.nextInt();
		}		
		int i = n-1;
		while(sum < k) {
			if (k_clone >= coin[i]) {
				check++;
				sum = sum + coin[i];
				k_clone = k_clone - coin[i];				
				if (k_clone < coin[i]) {
					i--;
				}
			}			
			else {
				i--;
			}
		}
		System.out.print(check);
	}
}
