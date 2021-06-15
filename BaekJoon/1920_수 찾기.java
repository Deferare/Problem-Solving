import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr1 = new int[n];
        for (int i = 0; i < arr1.length; i++) {
            arr1[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int[] arr2 = new int[m];
        for (int i = 0; i < arr2.length; i++) {
            arr2[i] = sc.nextInt();
        }
        for (int i = 0; i < m; i++) {
            int check = 0;
            for (int j = 0; j < n; j++) {
                if (arr2[i] == arr1[j]) {
                    System.out.println(1);
                    check = 1;
                    break;
                }
            }
            if (check == 0) System.out.println(0);
        }
    }
}
