import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int n = sc.nextInt(); int k = sc.nextInt();
		int sum = 0;
		for (int i = 1; i <= k; i++) {
			int a = (n*i);
			String s = "";
			int check = 0;
			if (a < 10)
				sum = a;
			else if (a < 100) {
				s = a+"";
				s = s.charAt(1)+""+s.charAt(0);
				check = Integer.parseInt(s);
			}
			else if (a < 1000) {
				s = a+"";
				s = s.charAt(2)+""+s.charAt(1)+""+s.charAt(0);
				check = Integer.parseInt(s);
			}
			else if (a < 10000) {
				s = a+"";
				s = s.charAt(3)+""+s.charAt(2)+""+s.charAt(1)+""+s.charAt(0);
				check = Integer.parseInt(s);
			}
			else if (a < 100000) {
				s = a+"";
				s = s.charAt(4)+""+s.charAt(3)+""+s.charAt(2)+""+s.charAt(1)+""+s.charAt(0);
				check = Integer.parseInt(s);
			}
			else if (a < 1000000) {
				s = a+"";
				s = s.charAt(5)+""+s.charAt(4)+""+s.charAt(3)+""+s.charAt(2)+""+s.charAt(1)+""+s.charAt(0);
				check = Integer.parseInt(s);
			}
			if (check > sum) {
				sum = check;
			}
		}
		System.out.println(sum);
	}
}
