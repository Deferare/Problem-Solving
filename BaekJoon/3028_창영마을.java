import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String save = sc.nextLine();
        int[] location = {1,0,0};
        for (int i = 0; i < save.length(); i++) {
            if (save.charAt(i) == 'A') {
                int tmp = location[0];
                location[0] = location[1];
                location[1] = tmp;
            }
            else if (save.charAt(i) == 'B') {
                int tmp = location[1];
                location[1] = location[2];
                location[2] = tmp;
            }
            else if (save.charAt(i) == 'C') {
                int tmp = location[0];
                location[0] = location[2];
                location[2] = tmp;
            }
        }
        for (int i = 0; i < location.length; i++) {
            if (location[i] > 0) {
                System.out.println(i+1);
            }
        }
    }
}
