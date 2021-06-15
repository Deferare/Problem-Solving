import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt(); sc.nextLine();
        for (int i = 0; i < testCase; i++) {
            String str = sc.nextLine();
            String save = "";
            if (str.charAt(0) > 90) {
                int tmp = str.charAt(0)-32;
                char tmp2 = (char)tmp;
                save += Character.toString(tmp2);
            }else {
                save += str.charAt(0);
            }
            for (int j = 1; j < str.length(); j++) {
                save += str.charAt(j);
            }
            System.out.println(save);
        }
    }
}
