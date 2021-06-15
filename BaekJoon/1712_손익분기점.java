import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();
		long i = 0; int check = 0;		
		if (c <= b) System.out.println(-1);
		else System.out.println(a/(c-b) + 1);
	}
}
