import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int r1 = sc.nextInt(); int s = sc.nextInt();
        if (r1 > s) {
            int a = r1-s;
            System.out.println(s-a);
        }
        else if (r1 < s) {
            int a = s-r1;
            System.out.println(s+a);
        }
        else System.out.println(s);
    }
}
