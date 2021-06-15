import java.util.Scanner;
public final class Main {
    static int[] data = new int[21];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        int[] arr = new int[n.length()];
        for (int i = 0; i < n.length(); i++) {
            arr[i] = Character.getNumericValue(n.charAt(i));
        }
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = 0; j < arr.length-1; j++) {
                if (arr[j] < arr[j+1]) {
                    int tmp1 = arr[j]; int tmp2 = arr[j+1];
                    arr[j] = tmp2; arr[j+1] = tmp1;
                }
            }
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
    }
}
