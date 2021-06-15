import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //가게 수
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {//가게 정보 입력
        	arr[i] = sc.nextInt();
        }
        int check = 0; int player = 0;
        for (int i = 0; i < arr.length; i++) {
        	if (player == arr[i]) {
        		check++;
        		if (arr[i] == 0) player = 1;
        		else if (arr[i] == 1) player = 2;
        		else if (arr[i] == 2) player = 0;
        	}
        }
        System.out.print(check);
	}
}
