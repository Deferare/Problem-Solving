class Solution {
    public String solution(String[] seoul) {
        int i = 0;
        while (true) {
            if (seoul[i].equals("Kim")) {
                break;
            }
            i++;
        }
        String result = "김서방은"+" "+i+"에 있다";
        return result;
    }
}
