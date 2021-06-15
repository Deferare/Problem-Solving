class Solution {
    public boolean solution(int x) {
        String save = x+"";
        int sum = 0;
        for (int i = 0; i < save.length(); i++) {
            sum += Character.getNumericValue(save.charAt(i));
        }
        if (x%sum != 0) return false;
        return true;
    }
}
