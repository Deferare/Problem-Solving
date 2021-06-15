import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		while (true) {
			String n = sc.nextLine(); int j = n.length()-1; int check = 0;
			int n1 = Integer.parseInt(n);
			if (n1 == 0) break;
			for (int i = 0; i < n.length()/2; i++, j--) {
				if (n.charAt(i) != n.charAt(j)) {
					check = 1; break;
				}					
			}
			if (check == 0)
				System.out.println("yes");
			else if (check == 1)
				System.out.println("no");
		}		
	}
}
