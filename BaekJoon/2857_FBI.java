import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); int turn = 0;
        for (int i = 0; i < 5; i++) {
            String str = sc.nextLine();
            for (int j = 0; j <= str.length()-3; j++) {
                if (str.charAt(j) == 'F') {
                    if (str.charAt(j+1) == 'B' && str.charAt(j+2) == 'I') {
                        if (turn == 1) System.out.print(" ");
                        System.out.print(i+1);
                        turn = 1;
                        break;
                    }
                }
            }
        }
        if (turn == 0) System.out.println("HE GOT AWAY!");
    }
}
