import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int n1 = sc.nextInt(); String s = sc.next();
            for (int j = 0; j < s.length(); j++) {
                for (int k = 0; k < n1; k++) {
                    System.out.print(s.charAt(j));
                }
            }
            System.out.println();
        }
    }
}
