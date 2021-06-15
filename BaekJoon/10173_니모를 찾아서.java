import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String checkStr = ""; int checkInt = 0;
        while(true) {
            String str = sc.nextLine();
            if (str.equals("EOI")) break;
            checkInt++; int check = 0;
            for (int i = 0; i < str.length()-2; i++) {
                if (str.charAt(i) == 'n' || str.charAt(i) == 'N') {
                    if (str.charAt(i+1) == 'e' || str.charAt(i+1) == 'E') {
                        if (str.charAt(i+2) == 'm' || str.charAt(i+2) == 'M') {
                            if (str.charAt(i+3) == 'o' || str.charAt(i+3) == 'O') {
                                check = 1;
                            }
                        }
                    }
                }
            }
            if (check == 1) checkStr += "Foundㅗ";
            else checkStr += "Missingㅗ";
        }
        String[] arr = new String[checkInt];
        String saveStr = ""; int index = 0;
        for (int i = 0; i < checkStr.length(); i++) {
            if (checkStr.charAt(i) != 'ㅗ')
                saveStr += checkStr.charAt(i);
            if (checkStr.charAt(i) == 'ㅗ') {
                arr[index] = saveStr; index++;
                saveStr = "";
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i != arr.length-1) System.out.println();
        }
    }
}
