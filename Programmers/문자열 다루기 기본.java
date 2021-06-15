class Solution {
    public boolean solution(String s) {
        if (s.length() != 4 && s.length() != 6) return false;
        for (int i = 0; i < s.length(); i++) {
            int check = 0;
            for (int j = 0; j < 10; j++) {
                if (Character.getNumericValue(s.charAt(i)) == j) {
                    check = 1; break;
                }
            }
            if (check == 0) return false;
        }
        return true;
    }
}
