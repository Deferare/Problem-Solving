class Solution {
    public long solution(int a, int b) {
        long result = 0;
        if (b > a) {
            for (int i = a; i <= b; i++) {
                result += i;
            }
        }
        else {
            for (int i = b; i <= a; i++) {
                result += i;
            }
        }

        return result;
    }
}
