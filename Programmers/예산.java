class Solution {
    public int solution(int[] d, int budget) {
        for (int i = 0; i < d.length-1; i++) {
            for (int j = 0; j < d.length-1; j++) {
                if (d[j] > d[j+1]) {
                    int tmp1 = d[j]; int tmp2 = d[j+1];
                    d[j+1] = tmp1; d[j] = tmp2;
                }
            }
        }       
        int check = 0; int sum = 0;
        for (int i = 0; i < d.length; i++) {
            if (sum+d[i] <= budget) {
                sum += d[i];
                check++;
            }
            else break;
        }
        return check;
    }
}
