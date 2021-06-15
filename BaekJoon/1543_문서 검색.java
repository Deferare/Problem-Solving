import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();  String str2 = sc.nextLine();
        int check = 0;
        for (int i = 0; i <= str1.length()-str2.length(); i++) {
            if (str1.charAt(i) == str2.charAt(0)) {
                int turn = 0;
                for (int j = 1; j < str2.length(); j++) {
                    if (str1.charAt(i+j) != str2.charAt(j)) {
                        turn = 1;
                    }
                }
                if (turn == 0) {
                    check++;
                    i = i+str2.length()-1;
                }
            }
        }
        System.out.println(check);
    }
}
