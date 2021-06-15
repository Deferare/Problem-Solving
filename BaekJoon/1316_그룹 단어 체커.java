import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);		
		int cycle = sc.nextInt();		
		int count = cycle;
		
		for (int i = 0; i <= cycle; i++) {
			boolean[] check = new boolean[26];
			String word = sc.nextLine();
			for (int j = 1; j < word.length(); j++) {
				if (word.charAt(j) != word.charAt(j-1)) {
					if (check[word.charAt(j)-'a'] == true) {
						count--;
						break;
					}
					check[word.charAt(j-1)-'a'] = true;					
				}				
			}
		}
		System.out.println(count);
	}
}
