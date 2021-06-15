import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            int check = 0;
            if (str.charAt(i) != ' ') {
                if (str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u' && i != 0) {
                    if (str.charAt(i) == str.charAt(i+2) && str.charAt(i+1) == 'p') {
                        check = 1;
                    }
                }
            }
            result += str.charAt(i);
            if (check == 1) {
                i+=2;
            }
        }
        System.out.println(result);
    }
}
