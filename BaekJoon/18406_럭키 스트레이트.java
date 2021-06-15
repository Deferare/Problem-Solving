import java.util.Scanner;
public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        int sum1 = 0; int sum2 = 0;
        int j = n.length()-1;
        for (int i = 0; i < n.length()/2; i++,j--) {
            sum1 += Character.getNumericValue(n.charAt(i));
            sum2 += Character.getNumericValue(n.charAt(j));
        }
        if (sum1 == sum2) {
            System.out.print("LUCKY");
        }
        else System.out.print("READY");
    }
}
