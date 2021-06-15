import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        String[] str = new String[n];
        for (int i = 0; i < str.length; i++) {
            str[i] = sc.nextLine();
        }
        String result = str[0];
        for (int i = 1; i < str.length; i++) {
            String save = "";
            for (int j = 0; j < str[i].length(); j++) {
                if (result.charAt(j) == str[i].charAt(j)) {
                    save += str[i].charAt(j);
                }
                else if (result.charAt(j) != str[i].charAt(j)) {
                    save += "?";
                }
            }
            result = save;
        }
        System.out.print(result);
    }
}
