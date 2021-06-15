import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String str = sc.nextLine();
            if (str.equals("end")) break;
            int vowelCheck = 0; int vowelSuccessionCheck = 0; int vowelSuccessionCheck2 = 0;
            int susccessCheck = 0;
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u') {
                    susccessCheck = 0; vowelCheck = 1;
                    if (i < str.length()-2) {
                        if (str.charAt(i+1) == 'a' || str.charAt(i+1) == 'e' || str.charAt(i+1) == 'i' || str.charAt(i+1) == 'o' || str.charAt(i+1) == 'u') {
                            if (str.charAt(i+2) == 'a' || str.charAt(i+2) == 'e' || str.charAt(i+2) == 'i' || str.charAt(i+2) == 'o' || str.charAt(i+2) == 'u') {
                                vowelSuccessionCheck = 1;
                            }
                        }
                    }
                }
                else {
                    susccessCheck++;
                }
                if (susccessCheck == 3) {
                    break;
                }
                if (i < str.length()-1) {
                    if (str.charAt(i) != 'e' && str.charAt(i) != 'o') {
                        if (str.charAt(i) == str.charAt(i+1)) {
                            vowelSuccessionCheck2 = 1;
                            break;
                        }
                    }
                }
            }
            if (vowelCheck == 1 && vowelSuccessionCheck == 0 && vowelSuccessionCheck2 == 0 && susccessCheck < 3)
                System.out.printf("<%s> is acceptable.%n",str);
            else {
                System.out.printf("<%s> is not acceptable.%n",str);
            }
        }
    }
}
