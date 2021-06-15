import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next(); String str2 = sc.next();
        long sum = 0;
        for (int i = 0; i < str1.length(); i++) {
            for (int j = 0; j < str2.length(); j++) {
                int a = Character.getNumericValue(str1.charAt(i)); int b = Character.getNumericValue(str2.charAt(j));
                sum += a*b;
            }
        }
        System.out.println(sum);
    }
}
