import java.math.BigInteger;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next(); String b = sc.next();
        BigInteger numA = new BigInteger(a); BigInteger numB = new BigInteger(b);
        System.out.print(numA.add(numB));
    }
}
