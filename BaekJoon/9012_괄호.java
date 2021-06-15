import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            int stateCnt = 0;
            int check = 0;
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == '(') stateCnt++;
                else if (str.charAt(j) == ')') stateCnt--;
                if (stateCnt < 0) {
                    check = 1;
                    break;
                }
            }
            if (check == 0 && stateCnt == 0) {
                result[i] = "YES";
            }
            else {
                result[i] = "NO";
            }
        }
        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
    }
}
