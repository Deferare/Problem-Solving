import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int sum = 0; int cnt = 0;
        int left = 0; int right = 0;
        while (true) {
            for (int i = left; i <= right; i++) {
                sum += arr[i];
            }
            if (sum < m)
                right++;
            else if (sum > m)
                left++;
            else if (sum == m)  {
                cnt++;
                right++;
            }
            if (right == arr.length) break;
            sum = 0;
        }
        System.out.print(cnt);
    }
}
