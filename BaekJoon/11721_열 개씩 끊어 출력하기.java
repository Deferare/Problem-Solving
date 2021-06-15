import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);		
		String arr = sc.nextLine(); int check = 0;
		while(true) {	
			char[] arrA = new char[10];int s = 0;
			if (arr.length()-check > 10) {
				for (int i = check; i < check + 10; i++) {	
					arrA[s] = arr.charAt(i);
					s++;
				}				
				System.out.println(arrA);				
			}
			else if (arr.length()-check <= 10){
				for (int i = check; i < arr.length(); i++) {
					System.out.print(arr.charAt(i));
				}
				break;
			}
			check += 10;			
		}
	}
}
