class Solution {
    public int[] solution(int[] arr) {
        int min = 100000;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) min = arr[i];
        }
        int[] result = new int[arr.length-1]; int index = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != min) {
                result[index] = arr[i];
                index++;
            }
        }
        if (result.length == 0) {
            int[] second = {-1};
            return second;
        }
        return result;
    }
}
