import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (i > 99) {
                int check = 0;
                String save = i + "";
                int firstN = 0;
                if (Character.getNumericValue(save.charAt(0)) > Character.getNumericValue(save.charAt(1)))
                    firstN = Character.getNumericValue(save.charAt(0)) - Character.getNumericValue(save.charAt(1));
                else firstN = Character.getNumericValue(save.charAt(1)) - Character.getNumericValue(save.charAt(0));
                for (int j = 1; j < save.length()-1; j++) {
                    int saveN = 0;
                    if (Character.getNumericValue(save.charAt(j)) > Character.getNumericValue(save.charAt(j+1)))
                        saveN = Character.getNumericValue(save.charAt(j)) - Character.getNumericValue(save.charAt(j+1));
                    else saveN = Character.getNumericValue(save.charAt(j+1)) - Character.getNumericValue(save.charAt(j));
                    if (firstN != saveN || save.charAt(0) == save.charAt(j+1)) {
                        int checkSub = 0;
                        for (int k = 1; k < save.length(); k++) {
                            if (Character.getNumericValue(save.charAt(0)) != Character.getNumericValue(save.charAt(k))) {
                                checkSub = 1;
                            }
                        }
                        if (checkSub == 0) continue;
                        check = 1;
                        break;
                    }
                }
                if (check == 0) {
                    cnt++;
                }
            }
            else cnt++;
        }
        System.out.print(cnt);
    }
}
