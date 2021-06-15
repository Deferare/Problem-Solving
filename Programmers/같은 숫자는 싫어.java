import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] save = new int[arr.length];
        int check = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i != arr.length-1 && arr[i] != arr[i+1]) {
                save[check] = arr[i];   check++;
            }
            if (i == arr.length-1) {
                save[check] = arr[i];   check++;
            }
        }
        int[] answer = new int[check];
        for (int i = 0; i < check; i++) {
            answer[i] = save[i];
        }
        return answer;
    }
}
