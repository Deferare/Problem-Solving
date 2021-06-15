import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = n;
        int min = n;
        while (true) {
            String str = num+"";
            int saveInt = num;
            for (int i = 0; i < str.length(); i++) {
                saveInt += Character.getNumericValue(str.charAt(i));
            }
            if (saveInt == n && num < min) {
                min = num;
            }
            if (saveInt <= n/2) {
                break;
            }
            num--;
        }
        if (min == n) System.out.print(0);
        else System.out.print(min);
    }
}
