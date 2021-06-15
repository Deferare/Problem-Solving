import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next().toUpperCase();
		int[] arr = new int[26];		
		int max = 0, num;
		char result = '?';
		for (int i = 0; i < s.length(); i++) {
			num = s.charAt(i)-65;
			arr[num]++;
		}		
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] > max) {
				max = arr[i];
				result = (char)(i+65);
			}
			else if (max == arr[i]) result = '?';
		}
		System.out.println(result);
	}
}
