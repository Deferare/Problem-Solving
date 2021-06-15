import java.util.Scanner;
public class Main {
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);	
		int[] arr = new int[10];	
		int[] arrS = new int[42];
		int di = 42;
		int count = 0;
		for (int i = 0; i < 10; i++) {
			arr[i] = scan.nextInt();
			arr[i] = arr[i]%di;
			arrS[arr[i]]++;
			if (arrS[arr[i]] == 1) {
				count++;
			}
		}	
		System.out.println(count);	
	}
}
