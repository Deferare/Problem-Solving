import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] stack = new int[n];
		for (int i = 0; i < n; i++) {
			int num = sc.nextInt();
			if (num != 0) stack[i] = num;
			else if (num == 0)  {
				for (int j = i; j >= 0; j--) {
					if (stack[j] > 0) {
						stack[j] = 0;
						break;
					}
				}
			}
		}
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += stack[i];
		}
		System.out.print(sum);
	}	
}
