import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String main = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int testCase = sc.nextInt(); sc.nextLine();
        for (int i = 0; i < testCase; i++) {
            int sum = 0;
            String str = sc.nextLine();
            for (int j = 0; j < main.length(); j++) {
                int check = 0;
                for (int k = 0; k < str.length(); k++) {
                    if (main.charAt(j) == str.charAt(k)) {
                        check = 1;
                        break;
                    }
                }
                if (check == 0) {
                    sum += main.charAt(j);
                }
            }
            System.out.println(sum);
        }
    }
}
