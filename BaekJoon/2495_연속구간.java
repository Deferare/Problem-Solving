import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            String str = sc.next();
            long check = 1; long sum = 0;
            for (int j = 0; j < str.length()-1; j++) {
                if(str.charAt(j) == str.charAt(j+1) ) {
                    check++;
                }
                else check = 1;
                if(sum < check) sum = check;
            }
            if (sum == 0) System.out.println(1);
            else {
                System.out.println(sum);
            }
        }
    }
}
