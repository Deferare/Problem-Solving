import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            int sum = 0; String saveStr = "";
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) != ' ') {
                    saveStr += str.charAt(j);
                }
                if (str.charAt(j) == ' ' || j == str.length()-1) {
                    sum += Integer.parseInt(saveStr);
                    saveStr = "";
                }
            }
            System.out.println(sum);
        }
    }
}
