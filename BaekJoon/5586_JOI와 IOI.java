import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int joiN = 0; int ioiN = 0;
        for (int i = 0; i < str.length()-2; i++) {
            if (str.charAt(i) == 'J' || str.charAt(i) == 'I') {
                if (str.charAt(i) == 'J' && str.charAt(i+1) == 'O' && str.charAt(i+2) == 'I') {
                    joiN++;
                }
                else if (str.charAt(i) == 'I' && str.charAt(i+1) == 'O' && str.charAt(i+2) == 'I') {
                    ioiN++;
                }
            }
        }
        System.out.println(joiN);
        System.out.println(ioiN);
    }
}
