public class Main {
    public static void main(String[] args) {
        int[] arr = new int[10036];
        for (int i = 1; i < 10000; i++) {
            arr[i] = i;
        }
        int n = 1;
        while (true) {
            int nextN = n;
            String saveN = n+"";
            for (int i = 0; i < saveN.length(); i++) {
                nextN += Character.getNumericValue(saveN.charAt(i));
            }
            arr[nextN] = -1;
            n++;
            if (n >= 10000) break;
        }
        for (int i = 1; i <= 10000; i++){
            if (arr[i] > 0) System.out.println(arr[i]);
        }
    }
}
