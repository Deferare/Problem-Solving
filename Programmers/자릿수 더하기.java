import java.util.*;

public class Solution {
    public int solution(int n) {
        String save = n+""; int sum = 0;
        for (int i = 0; i < save.length(); i++) {
            sum += Integer.parseInt(String.valueOf(save.charAt(i)));
        }
        return sum;
    }
}
