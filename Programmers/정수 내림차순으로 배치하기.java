class Solution {
    public long solution(long n) {
        String length = n+""; int sum = 0;
        int[] save = new int[length.length()];
        for (int i = 0; i < length.length(); i++) {
            save[i] += Integer.parseInt(String.valueOf(length.charAt(i)));            
        }
        for (int i = 0; i < save.length-1; i++) {
            for (int j = 0; j < save.length-1; j++) {
                if (save[j] < save[j+1]) {
                    int tmp = save[j]; int tmp2 = save[j+1];
                    save[j] = tmp2; save[j+1] = tmp;
                }
            }
        }
        length = "";
        for (int i = 0; i < save.length; i++) {
            length += save[i];
        }
        long result = Long.parseLong(length);
        return result;
    }
}
