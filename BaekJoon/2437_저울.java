import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr); int check = 0;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            if (sum+1 < arr[i]) {
                System.out.println(sum+1);
                check = 1;
                break;
            }
            sum += arr[i];
        }
        if (check == 0)
            System.out.println(sum+1);
    }
}
