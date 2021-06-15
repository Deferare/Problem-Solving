import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String result = ""; String save1 = ""; String save2 = "";
        int turn = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '<') {
                if (save1.length() > 0) {
                    String strSave = "";
                    for (int j = save1.length()-1; j >= 0; j--) {
                        strSave += save1.charAt(j);
                    }
                    result += strSave;
                    save1 = "";
                }
                turn = 1;
            }
            if (str.charAt(i) == '>' && turn == 1) {
                save2 += str.charAt(i);
                result += save2;
                save2 = "";
                turn = 0;
            }
            if (turn == 0 && str.charAt(i) != '>') {
                save1 += str.charAt(i);
            }
            else if (turn == 1) {
                save2 += str.charAt(i);
            }
            if (turn == 0 && str.charAt(i) == ' ' || i == str.length()-1) {
                if (str.charAt(i) == ' ') {
                    String strSave = "";
                    for (int j = save1.length()-2; j >= 0; j--) {
                        strSave += save1.charAt(j);
                    }
                    strSave += " ";
                    result += strSave;
                    save1 = "";
                }
                else if (i == str.length()-1) {
                    String strSave = "";
                    for (int j = save1.length()-1; j >= 0; j--) {
                        strSave += save1.charAt(j);
                    }
                    result += strSave;
                }
            }
        }
        System.out.println(result);
    }
}
