import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //유제품 수
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) { //유제품 개별 가격
        	arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        int sum = 0; int i1 = 0;
        for (int i = arr.length; i >= 1; i--, i1++) {        	
        	if (i1%3 != 0 && i != arr.length) {
            	sum += arr[i];
           	}         	        	
        }
        System.out.println(sum);
	}
}
