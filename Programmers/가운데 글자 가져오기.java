class Solution {
    public String solution(String s) {
        if (s.length()%2 != 0) {
            return Character.toString(s.charAt(s.length()/2));
        }
        else if (s.length()%2 == 0) {
            return s.charAt(s.length()/2-1)+Character.toString(s.charAt(s.length()/2));
        }
        return "흠;";
    }
}
