class Solution {
    public int[] solution(int[] prices) {
        int[] result = new int[prices.length];
        for (int i = 0; i < prices.length-1; i++) {
            int check = 1;
            for (int j = i+1; j < prices.length-1; j++) {
                if (prices[i] <= prices[j]) {
                    check++;
                }
                else break;
            }
            result[i] = check;
        }
        result[result.length-1] = 0;
        return result;
    }
}
