import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt(); sc.nextLine();
        String[] result = new String[testCase];
        for (int i = 0; i < testCase; i++) {
            String str = sc.nextLine();
            int k = str.length()-1;
            for (int j = 0; j < str.length()/2; j++, k--) {
                int check = 0;
                if (str.charAt(j) == str.charAt(k)) {
                    check = 1;
                }
                else if (str.charAt(j)-32 == str.charAt(k)) {
                    check = 1;
                }
                else if (str.charAt(j) == str.charAt(k)-32) {
                    check = 1;
                }
                else {
                    k = 0;
                    result[i] = "No"; break;
                }
            }
            if (k != 0) result[i] = "Yes";
        }
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i != result.length-1) System.out.println();
        }
    }
}
