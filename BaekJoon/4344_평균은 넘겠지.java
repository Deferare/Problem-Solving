import java.util.*;
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int c = sc.nextInt();
		int[] arr;		
		for (int i = 0; i < c; i++) {
			int overall = 0;
			int count = 0;
			int num = sc.nextInt();
			arr = new int[num+1];
			arr[0] = num; //학생 수 입력			
			for (int j = 1; j <= arr[0]; j++) {
				arr[j] = sc.nextInt(); //개별 학생 점수 입력
				overall += arr[j]; // overall에 점수 누적
			}					
			int k = 0;
			do {
				k++;
				if (overall/arr[0] < arr[k]) { //평균보다 높은 점수의 학생 수 카운트
					count++;
				}
				if (arr[0] == k) {
					String avg = String.format("%.3f",(float)count/arr[0]*100);					
					System.out.println(avg+"%");
					break;
				}
			} while(true);			
		}		
	}
}
