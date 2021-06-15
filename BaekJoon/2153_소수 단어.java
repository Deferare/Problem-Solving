import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String save = sc.nextLine();
        int sum = 0;
        for (int i = 0; i < save.length(); i++) {
            if (save.charAt(i) <= 90) {
                sum += save.charAt(i)-64;
            }
            else if (save.charAt(i) > 90) {
                sum += save.charAt(i)-96;
            }
        }        
        int check = 0;
        for (int i = 2; i <= sum/2; i++) {
            if (sum%i == 0) {
                check = 1;
            }
        }
        if (check == 0 || sum == 1) {
            System.out.println("It is a prime word.");
        }
        else {
            System.out.println("It is not a prime word.");
        }
    }
}
