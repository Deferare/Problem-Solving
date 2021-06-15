import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		int sum = 0;
		int check = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == ' ') {				 				
				sum++;
			}			
		
		}		
		if (s.charAt(0) == ' ') sum--; 
		if (s.charAt(s.length()-1) == ' ') sum--;
		System.out.println(sum+1);
	}
}
