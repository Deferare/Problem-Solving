import java.util.Scanner;
public class Main {
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);	
		int n = scan.nextInt();
		String[] arr = new String[n+1];
		int[] result = new int[n+1];	
		int check = 0;
		for (int i = 0; i <= arr.length+1; i++) {			
			int score = 0;
			result[i] = 0;	
			arr[i] = scan.nextLine();		
			for (int j = 0; j < arr[i].length(); j++) {				
				if (arr[i].charAt(j) == 'O') {
					score++;
					result[i] += score;
				}
				else if (arr[i].charAt(j) == 'X'){
					score = 0;
					check = 1;
				}				
			}	
			if (i == arr.length-1) break;
		}
		for (int i = 1; i < result.length; i++) {			
			if (result[i] != 0 || check == 1) System.out.println(result[i]);
		}
	}
}
