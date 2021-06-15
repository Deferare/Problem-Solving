class Solution {
    public String solution(String phone_number) {
        String save = ""; int num = phone_number.length()-4;
        for (int i = 0; i < num; i++) {
            save += '*';
        }
        for (int j = phone_number.length()-4; j < phone_number.length(); j++) {
            save += phone_number.charAt(j);
        }
        return save;
    }
}
