import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr1 = new int[n]; int[] arr2 = new int[n];
        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            arr2[i] = sc.nextInt();
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int maxSave = 0; int minSave = 101; int numIndexSave = 0;
            for (int j = 0; j < n; j++) {
                if (arr2[j] >= maxSave) {
                    maxSave = arr2[j];
                    numIndexSave = j;
                }
            }
            arr2[numIndexSave] = 0;
            for (int j = 0; j < n; j++) {
                if (arr1[j] < minSave) {
                    minSave = arr1[j];
                    numIndexSave = j;
                }
            }
            arr1[numIndexSave] = 101;
            sum += (maxSave*minSave);
        }
        System.out.print(sum);
    }
}
