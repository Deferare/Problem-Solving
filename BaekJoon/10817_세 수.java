import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt(); int n2 = sc.nextInt(); int n3 = sc.nextInt();
        int[] arr = {n1,n2,n3};
        if (n1 > n2 && n2 > n3) System.out.println(n2);
        else if (n1 < n2 && n2 < n3) System.out.println(n2);
        else if (n2 > n1 && n1 > n3) System.out.println(n1);
        else if (n2 < n1 && n1 < n3) System.out.println(n1);
        else if (n2 > n3 && n3 > n1) System.out.println(n3);
        else if (n2 < n3 && n3 < n1) System.out.println(n3);
        else {
            for (int i = 0; i < 3; i++) {
                int check = 0;
                for (int j = 0; j < 3; j++) {
                    if (arr[i] == arr[j]) {
                        check++;
                    }
                }
                if (check >= 2) {
                    System.out.println(arr[i]);
                    break;
                }
            }
        }
    }
}
