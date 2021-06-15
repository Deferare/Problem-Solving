import java.util.Scanner;
public final class Main {
    static int[] data = new int[21];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(fabo(n));
    }
    public static int fabo(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        if (data[n] != 0)
            return data[n];
        return data[n] = fabo(n-1) + fabo(n-2);
    }
}
