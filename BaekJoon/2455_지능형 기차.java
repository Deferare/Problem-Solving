import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] train = new int[8];
		for (int i = 0; i < train.length; i++) {
			train[i] = sc.nextInt();
		}
		int personnel  = train[1]; int max = 0; int turn = 0; 
		for (int i = 2; i < train.length-2; i++) {
			if (turn == 0) {
				personnel -= train[i];
				turn = 1;
			}
			else if (turn == 1) {
				personnel += train[i];
				turn = 0;
				if (personnel > max) max = personnel;
			}
		}
		System.out.println(max);
	}
}
