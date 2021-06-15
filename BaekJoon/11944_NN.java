import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int m = sc.nextInt();
        String save = ""; int check = 0;
        for (int i = 0; i < n; i++) {
            save += n+"";
            if (save.length() > m) {
                check = 1;
                break;
            }
        }
        String save2 = "";
        if (check == 0)
            System.out.print(save);
        else {
            for (int i = 0; i < m; i++) {
                save2 += save.charAt(i);
            }
            System.out.println(save2);
        }
    }
}
