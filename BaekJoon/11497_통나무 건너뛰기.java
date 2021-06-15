import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);			
		int testCase = sc.nextInt();		
		for (int i = 0; i < testCase; i++) {
			int logNum = sc.nextInt();
			int[] log = new int[logNum];
			int[] logarr = new int[logNum];
			for (int j = 0; j < logNum; j++) {
				log[j] = sc.nextInt();
			}
			Arrays.sort(log); int a = 0; int b = logNum-1; int turn = 0;
			for (int j = 0; j < logNum; j++) {
				if (turn == 0) {
					logarr[a] = log[j];
					turn = 1;
					a++;
				}
				else if (turn == 1) {
					logarr[b] = log[j];
					turn = 0;
					b--;
				}
			}
			int mi = 0;
			for (int j = 0; j < logNum; j++) { 
				if (j < logNum/2) { 
					if (mi < logarr[j+1] - logarr[j]) {
						mi = logarr[j+1] - logarr[j];
					}
				}
				else if (j < logNum-1) {
					if (mi < logarr[j] - logarr[j+1]) {
						if (j != logNum-1) {
							mi = logarr[j] - logarr[j+1];
						}												
					}					
				}
				else if (j == logNum-1) {
					if (logarr[j] > logarr[0]) {
						if (mi < logarr[j] - logarr[0])
							mi = logarr[j] - logarr[0];
					}								
					else if (logarr[j] < logarr[0]) {
						if (mi < logarr[0] - logarr[j])
							mi = logarr[0] - logarr[j];								
					}								
				}
			}
			System.out.println(mi);
 		}
	}
}
