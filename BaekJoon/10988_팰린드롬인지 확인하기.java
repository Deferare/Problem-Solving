import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);		
		String word = sc.nextLine(); int j = word.length()-1;
		int check = 1;
		for (int i = 0; i < word.length()/2; i++, j--) {
			if (word.charAt(i) != word.charAt(j)) {
				check = 0;
				break;
			}
		}
		System.out.print(check);
	}
}
