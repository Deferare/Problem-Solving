import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);			
		int n = sc.nextInt(); int m = sc.nextInt();
		int[] cardArr = new int[n];
		for (int i = 0; i < n; i++) {
			cardArr[i] = sc.nextInt();
		}
		int check = 0;
		for (int i = 0; i < n-2; i++) {
			for (int j = i+1; j < n-1; j++) {
				for (int k = j+1; k < n; k++) {
					if (cardArr[i] + cardArr[j] + cardArr[k] <= m && check < cardArr[i] + cardArr[j] + cardArr[k]) {
						check = cardArr[i] + cardArr[j] + cardArr[k]; 
					}
				}
			}
		}
		System.out.print(check);
	}
}
