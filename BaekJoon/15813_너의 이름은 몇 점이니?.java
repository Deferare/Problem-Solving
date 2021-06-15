import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   sc.nextLine();
        String name = sc.nextLine();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += name.charAt(i)-64;
        }
        System.out.print(sum);
    }
}
