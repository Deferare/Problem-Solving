import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int i;	
		int m = 0;		
		for (i = 0; i <= n; i++) {			
			m = m + i;			
		}
		System.out.println(m);
	}
}
