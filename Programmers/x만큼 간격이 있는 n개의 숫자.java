class Solution {
    public long[] solution(int x, int n) {
        long[] result = new long[n]; long sum = x;
        for (int i = 0 ; i < result.length; i++) {
            result[i] = sum;
            sum += x;
        }
        return result;
    }
}
