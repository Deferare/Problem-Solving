import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int k = sc.nextInt();
        Queue<Integer> data = new LinkedList<Integer>();
        for (int i = 0; i < n; i++) {
            data.offer(i+1);
        }
        String result = "<";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k-1; j++) {
                data.offer(data.poll());
            }
            result += data.poll();
            if (i != n-1) result += ", ";
        }
        System.out.println(result+">");
    }
}
