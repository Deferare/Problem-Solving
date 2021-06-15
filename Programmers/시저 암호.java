class Solution {
    public String solution(String s, int n) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') {
                int tmp = s.charAt(i);
                for (int j = 0; j < n; j++) {
                    tmp++;
                    if (tmp > 90 && tmp < 97 || tmp > 122) tmp -= 26;
                }
                char tmp2 = (char)tmp;
                result += tmp2;
            }
            else result += " ";
        }
        return result;
    }
}
