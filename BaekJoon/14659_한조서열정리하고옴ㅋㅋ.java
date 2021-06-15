import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int maxKill = 0;
        for (int i = 0; i < arr.length-1; i++) {
            int killSave = 0;
            for (int j = i+1; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    killSave++;
                }
                if (arr[i] < arr[j] || j == arr.length-1) {
                    if (killSave > maxKill) {
                        maxKill = killSave;
                    }
                    break;
                }
            }
        }
        System.out.print(maxKill);
    }
}
