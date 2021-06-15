import java.util.Scanner;
public final class Main {
    public static final void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int i = 0;
        int plus = 0;
        int minus = 0;
        String save = "";
        boolean turn = false;
        boolean var8;
        while(true) {
            if (i >= str.length()) {
                break;
            }
            if (!turn) {
                if (str.charAt(i) == '-') {
                    var8 = false;
                    plus += Integer.parseInt(save);
                    save = "";
                    turn = true;
                } else if (str.charAt(i) == '+') {
                    var8 = false;
                    plus += Integer.parseInt(save);
                    save = "";
                } else {
                    save = save + str.charAt(i);
                }

                if (i == str.length() - 1) {
                    var8 = false;
                    plus += Integer.parseInt(save);
                    break;
                }
            } else if (turn) {
                if (str.charAt(i) == '+') {
                    var8 = false;
                    minus += Integer.parseInt(save);
                    save = "";
                } else if (str.charAt(i) == '-') {
                    var8 = false;
                    minus += Integer.parseInt(save);
                    save = "";
                } else {
                    save = save + str.charAt(i);
                }

                if (i == str.length() - 1) {
                    var8 = false;
                    minus += Integer.parseInt(save);
                    break;
                }
            }

            ++i;
        }
        int result;
        if (plus > minus) {
            result = plus - minus;
            var8 = false;
            System.out.print(result);
        } else {
            result = minus - plus;
            int var10 = result * -1;
            boolean var9 = false;
            System.out.print(var10);
        }
    }
}
