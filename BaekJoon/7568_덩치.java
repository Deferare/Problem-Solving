import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt(); arr[i][1] = sc.nextInt();
        }
        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i]++;
            for (int j = 0; j < arr.length; j++) {
                if (arr[i][0] < arr[j][0]) {
                    if (arr[i][1] < arr[j][1]) {
                        result[i]++;
                    }
                }
            }
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(result[i]);
            if (i != arr.length-1) System.out.print(" ");
        }
    }
}
