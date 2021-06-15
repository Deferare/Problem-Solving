class Solution {
    public int[] solution(long n) {
        String save = n+"";
        int[] result = new int[save.length()];
        int index = 0;
        for (int i = save.length()-1; i >= 0; i--) {
            result[index] = Character.getNumericValue(save.charAt(i));
            index++;
        }
        return result;
    }
}
