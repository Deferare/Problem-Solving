import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int n = sc.nextInt(); sc.nextLine();
        int result = 0;
        for (int i = 0; i < n; i++) {
            String ring = sc.nextLine();
            for (int j = 0; j < ring.length(); j++) {
                if (str.charAt(0) == ring.charAt(j)) {
                    int check = 0; int index = 0;
                    for (int k = j; k < j+str.length(); k++) {
                        if (k == ring.length()) {
                            k = 0;
                        }
                        if (ring.charAt(k) != str.charAt(index)) {
                            check = 1;
                            break;
                        }
                        index++;
                        if (index >= str.length()) break;
                    }
                    if (check == 0) {
                        result++;
                        break;
                    }
                }
            }
        }
        System.out.print(result);
    }
}
