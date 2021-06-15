import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next(); String b = sc.next();
        String answer = "";
        if (a.length() >= b.length()) {
            for (int i = 0; i < a.length()-b.length(); i++) {
                answer += a.charAt(i);
            }
            for (int i = a.length()-b.length(); i < a.length(); i++) {
                int tmp = Character.getNumericValue(a.charAt(i)) + Character.getNumericValue(b.charAt(i-(a.length()-b.length())));
                answer += tmp;
            }
            System.out.println(answer);
        }
        if (a.length() < b.length()) {
            for (int i = 0; i < b.length()-a.length(); i++) {
                answer += b.charAt(i);
            }
            for (int i = b.length()-a.length(); i < b.length(); i++) {
                int tmp = Character.getNumericValue(b.charAt(i)) + Character.getNumericValue(a.charAt(i-(b.length()-a.length())));
                answer += tmp;
            }
            System.out.println(answer);
        }
    }
}
