import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);		
		String word = sc.nextLine();
		String str = "";
		for (int i = 0; i < word.length(); i++) {
			if (word.charAt(i) <= 90 && word.charAt(i) != '-') {
				str += word.charAt(i);
			}
		}
		System.out.print(str);
	}
}
