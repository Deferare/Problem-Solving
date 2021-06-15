import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt(); sc.nextLine();
        String[] result = new String[testCase];
        for (int i = 0; i < testCase; i++) {
            String input = sc.nextLine();
            String str1 = ""; String str2 = "";
            int turn = 0;
            for (int j = 0; j < input.length(); j++) {
                if (input.charAt(j) == ' ') {
                    j++;
                    turn = 1;
                }
                if (turn == 0) str1 += input.charAt(j);
                else if (turn == 1) {
                    str2 += input.charAt(j);
                }
            }
            if (str1.length() == str2.length()) {
                int[] arr = new int[26];
                for (int j = 0; j < str1.length(); j++) {
                    ++arr[str1.charAt(j)-'a'];
                }
                int check = 0;
                for (int j = 0; j < str2.length(); j++) {
                    --arr[str2.charAt(j)-'a'];
                    if (arr[str2.charAt(j)-'a'] < 0) {
                        result[i] = str1+" & "+str2+" are NOT anagrams.";
                        //System.out.printf("%s & %s are NOT angarams.",str1,str2);
                        check = 1;
                        break;
                    }
                }
                if (check == 0) {
                    for (int j = 0; j < 26; j++) {
                        if (arr[j] < 0) {
                            result[i] = str1+" & "+str2+" are NOT anagrams.";
                            //System.out.printf("%s & %s are NOT angarams.",str1,str2);
                            check = 1;
                            break;
                        }
                    }
                }
                if (check != 1) {
                    result[i] = str1+" & "+str2+" are anagrams.";
                    //System.out.printf("%s & %s are angarams.",str1,str2);
                }
            }
            else {
                result[i] = str1+" & "+str2+" are NOT anagrams.";
                //System.out.printf("%s & %s are NOT angarams.",str1,str2);
            }
        }
        for (int i = 0; i < testCase; i++) {
            System.out.print(result[i]);
            if (i != testCase-1) System.out.println();
        }
    }
}
