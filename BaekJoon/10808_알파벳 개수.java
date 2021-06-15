import java.util.Scanner;
class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine();
		int[] result = new int['z'-96];
		for (int i = 0; i < word.length(); i++) {
			int check = 0;
			for (int j = 0; j < word.length(); j++) {
				if (word.charAt(i) == word.charAt(j))
					check++;
			}
			result[word.charAt(i)-97] = check;
		}
		for (int i = 0; i < result.length; i++) {
			System.out.print(result[i]);
			if (i != 25) {
				System.out.print(" ");
			}
		}
	}
}
