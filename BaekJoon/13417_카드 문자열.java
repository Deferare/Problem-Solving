import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCast = sc.nextInt(); sc.nextLine();
        String[] result = new String[testCast];
        for (int i = 0; i < testCast; i++) {
            int n = sc.nextInt(); sc.nextLine();
            String str = "";
            for (int j = 0; j < n; j++) {
                str += sc.next();
            }
            Deque data = new LinkedList();
            data.offerFirst(str.charAt(0));
            for (int j = 1; j < str.length(); j++) {
                int saveInt = (char) data.peek();
                if (str.charAt(j) <= saveInt) {
                    data.addFirst(str.charAt(j));
                }
                else if (str.charAt(j) > saveInt) {
                    data.addLast(str.charAt(j));
                }
            }
            String resultSave = "";
            while (!data.isEmpty()) {
                resultSave += (char)data.poll();
            }
            result[i] = resultSave;
        }
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i != result.length-1) System.out.println();
        }
    }
}
