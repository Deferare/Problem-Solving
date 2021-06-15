import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String mainStr = sc.nextLine(); String keyStr = sc.next();
        String result = ""; int index = 0;
        for (int i = 0; i < mainStr.length(); i++) {
            char tmp = mainStr.charAt(i);
            if (tmp != ' ') {
                for (int j = 0; j < keyStr.charAt(index)-'a'+1; j++) {
                    tmp--;
                    if (tmp < 'a') {
                        tmp = 'z';
                    }
                }
            }
            if (index == keyStr.length()-1) {
                index = 0;
            }
            else index++;
            result += tmp;

        }
        System.out.println(result);
    }
}
