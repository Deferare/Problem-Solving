import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String H = sc.nextLine(); String N = sc.nextLine();
        int check = 0;
        for (int i = 0; i < H.length()-(N.length()-1); i++) {
            if (H.charAt(i) == N.charAt(0)) {
                int index = 0; int subCheck = 0;
                for (int j = i; j < N.length()+i; j++) {
                    if (H.charAt(j) != N.charAt(index)) {
                        subCheck = 1;
                        break;
                    }
                    index++;
                }
                if (subCheck == 0) check++;
            }
        }
        System.out.print(check);
    }
}
