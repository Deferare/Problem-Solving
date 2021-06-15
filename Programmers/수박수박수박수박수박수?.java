class Solution {
    public String solution(int n) {
        int turn = 0;
        String result = "";
        for (int i = 0; i < n; i++) {
            if (turn == 0) {
                result += "수"; turn = 1;
            }
            else if (turn == 1) {
                result += "박"; turn = 0;
            }
        }
        return result;
    }
}
