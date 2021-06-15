class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] save = new int[arr.length]; int cnt = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]%divisor == 0) {
                cnt++;
                save[i] = arr[i];
            }
        }
        int[] result = new int[cnt]; int index = 0;
        int[] result2 = new int[1];
        if (cnt != 0) {
            for (int i = 0; i < save.length; i++) {
                if (save[i] > 0) {
                    result[index] = save[i]; index++;
                }
            }
        }
        else if (cnt == 0) {
            result2[0] = -1;
            return result2;
        }
        for (int i = 0; i < result.length-1; i++) {
            for (int j = 0; j < result.length-1; j++) {
                if (result[j] > result[j+1]) {
                    int tmp = result[j];
                    result[j] = result[j+1];
                    result[j+1] = tmp;
                }
            }
        }
        return result;
    }
}
