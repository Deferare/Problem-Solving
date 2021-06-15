import java.util.Scanner;
public class Main {	
	public static void main(String[] args){		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int check = n;
		if (n < 10) {
			n = n * 10;
			int n1 = n%10;
			int n10 = n/10;
			n = n1 + n10;
		}
		int sum = n;
		int sumM = 0;
		int count = 0;
		
		do {
			int n1 = sum%10;
			int n10 = sum/10;
			sum = n1 + n10;
			int sum1 = sum%10;
			String sumS =  n1+""+sum1;
			sum = Integer.parseInt(sumS);
			count++;
			if (sum == check) break;
		}while(true);
		System.out.println(count);
	}	
}
