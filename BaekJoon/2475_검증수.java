import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int[] arr = new int[5];
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            int a = sc.nextInt();
            if (a != 0)
                a *= a;
            sum += a;
        }
        System.out.println(sum%10);
    }
}
