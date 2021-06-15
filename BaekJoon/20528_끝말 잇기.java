import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        String str = sc.nextLine();
        int check = 0;
        for (int j = 0; j < str.length(); j++) {
            if (str.charAt(j) == ' ') {
                if (str.charAt(j+1) != str.charAt(0)) {
                    check = 1; break;
                }
            }
        }
        if (check == 0)
            System.out.print(1);
        else System.out.print(0);
    }
}
