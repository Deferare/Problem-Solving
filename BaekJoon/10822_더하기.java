import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine(); String save = "";
        int sum = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != ',') {
                save += Character.toString(str.charAt(i));
            }
            if (str.charAt(i) == ',' || i == str.length()-1) {
                int tmp = Integer.parseInt(save);
                sum += tmp;
                save = "";
            }
        }
        System.out.println(sum);
    }
}
