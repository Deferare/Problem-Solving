import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int leftCheck = 0; int rightCheck = 0; int turn = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') turn = 1;
            if (str.charAt(i) == '@') {
                if (turn == 0) leftCheck++;
                else if (turn == 1) rightCheck++;
            }
        }
        System.out.print(leftCheck +" "+ rightCheck);
    }
}
