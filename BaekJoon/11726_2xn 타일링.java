import java.util.Scanner;
public final class Main {
    public static int[] data = new int[1001];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fibo(n));
    }
    public static int fibo(int n) {
        if (1 == n) return 1;
        if (2 == n) return 2;
        if (data[n] != 0) return data[n];
        return data[n] = (fibo(n-1) + fibo(n-2))%10007;
    }
}
