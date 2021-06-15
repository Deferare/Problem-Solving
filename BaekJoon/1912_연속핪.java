import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int max = -1001; int tmp = -1001; int turn = 0;
        for (int i = 0; i < arr.length; i++) {
            if (tmp > arr[i] || tmp == -1001 || tmp < tmp+arr[i]) {
                if (tmp == -1001) tmp = 0;
                tmp += arr[i];
            }
            if (tmp <= arr[i]) {
                tmp = 0;
                tmp += arr[i];
            }
            if (tmp > max) max = tmp;
        }
        System.out.println(max);
    }
}
