import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String alpabet = sc.nextLine();
		int result = 0;
		for (int i = 0; i < alpabet.length(); i++) {
			 if (alpabet.charAt(i) == 'A' || alpabet.charAt(i) == 'B' || alpabet.charAt(i) == 'C') {
				 result = result + 3;
			 }
			 if (alpabet.charAt(i) == 'D' || alpabet.charAt(i) == 'E' || alpabet.charAt(i) == 'F') {
				 result = result + 4;
			 }
			 if (alpabet.charAt(i) == 'G' || alpabet.charAt(i) == 'H' || alpabet.charAt(i) == 'I') {
				 result = result + 5;
			 }
			 if (alpabet.charAt(i) == 'J' || alpabet.charAt(i) == 'K' || alpabet.charAt(i) == 'L') {
				 result = result + 6;
			 }
			 if (alpabet.charAt(i) == 'M' || alpabet.charAt(i) == 'N' || alpabet.charAt(i) == 'O') {
				 result = result + 7;
			 }
			 if (alpabet.charAt(i) == 'P' || alpabet.charAt(i) == 'Q' || alpabet.charAt(i) == 'R' || alpabet.charAt(i) == 'S') {
				 result = result + 8;
			 }
			 if (alpabet.charAt(i) == 'T' || alpabet.charAt(i) == 'U' || alpabet.charAt(i) == 'V') {
				 result = result + 9;
			 }
			 if (alpabet.charAt(i) == 'W' || alpabet.charAt(i) == 'X' || alpabet.charAt(i) == 'Y' || alpabet.charAt(i) == 'Z') {
				 result = result + 10;
			 }			 
		}
		System.out.print(result);
	}
}
