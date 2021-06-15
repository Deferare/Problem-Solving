import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String input = sc.next();
            if (input.charAt(0) == '#') {
                break;
            }
            String str = sc.nextLine();
            int check = 0;
            for (int i = 0; i < str.length(); i++) {
                if (input.charAt(0) == str.charAt(i) || input.charAt(0) == str.charAt(i)+32 || input.charAt(0) == str.charAt(i)-32) {
                    check++;
                }
            }
            System.out.print(input.charAt(0)+" "); System.out.println(check);
        }
    }
}
