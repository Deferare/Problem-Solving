import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt(); sc.nextLine();
        String[] result = new String[testCase];
        for (int i = 0; i < testCase; i++) {
            String sound = sc.nextLine();
            while (true) {
                String excepSound = "";
                String excepSave = sc.nextLine();
                if (!(excepSave.equals("what does the fox say?"))) {
                    int spaceCheck = 0;
                    for (int j = 0; j < excepSave.length(); j++) {
                        if (excepSave.charAt(j) == ' ')
                            spaceCheck++;
                        if (spaceCheck >= 2) {
                            if (spaceCheck == 2) {
                                j++; spaceCheck = 3;
                            }
                            excepSound += excepSave.charAt(j);
                        }
                    }
                    sound = strWordAllRemove(sound,excepSound);
                }
                else {
                    result[i] = sound;
                    break;
                }
            }
        }
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i != result.length-1) System.out.println();
        }
    }
    public static String strWordAllRemove(String str, String word) {
        String result = ""; String saveStr = "";
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != ' ') {
                saveStr += str.charAt(i);
            }
            if (str.charAt(i) == ' ' || i == str.length()-1) {
                if (saveStr.equals(word)) {

                }
                else {
                    result += saveStr;
                    if (i != str.length()-1) result += " ";
                }
                saveStr = "";
            }
        }
        return result;
    }
}
