class Solution {
    public String solution(String s) {
       String result = "";
        int turn = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                turn = 0;
                result += " ";
            }
            else if (turn == 0) {
                if (s.charAt(i) >= 97) {
                    char tmp = (char) (s.charAt(i)-32);
                    result += tmp;
                }
                else result += s.charAt(i);
                turn = 1;
            }
            else if (turn == 1) {
                if (s.charAt(i) <= 90) {
                    char tmp = (char) (s.charAt(i)+32);
                    result += tmp;
                }
                else result+= s.charAt(i);
                turn = 0;
            }
        }
        return result;
    }
}
