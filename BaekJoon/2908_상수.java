import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s1 = sc.nextLine();
		int a = Integer.parseInt(s1.charAt(2) + "" + s1.charAt(1) + "" +s1.charAt(0));
		int b = Integer.parseInt(s1.charAt(6) + "" + s1.charAt(5) + "" +s1.charAt(4));		
		if (a > b) System.out.print(a);
		if (a < b) System.out.print(b);
	}
}
