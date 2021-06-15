import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String str = sc.nextLine();
            if (str.equals("#")) break;
            int[] arr = new int[26]; int cnt = 0;
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) >= 65 && str.charAt(i) <= 90) {
                    if (arr[str.charAt(i)-65] == 0) {
                        arr[str.charAt(i)-65] = 1;
                        cnt++;
                    }
                }
                else if (str.charAt(i) >= 97 && str.charAt(i) <= 122) {
                    if (arr[str.charAt(i)-32-65] == 0) {
                        arr[str.charAt(i)-32-65] = 1;
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}
