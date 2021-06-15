class Solution {
    public String solution(String new_id) {
        int checkStr = 0;
        if (new_id.length() >= 3 && new_id.length() <= 15) {
            if (new_id.charAt(0) == '.' || new_id.charAt(new_id.length()-1) == '.') {
                checkStr = 1;
            }
            else {
                int periodCheck = 0;
                for (int i = 0; i < new_id.length(); i++) {
                    if (!((Character.getNumericValue(new_id.charAt(i)) >= 0 && Character.getNumericValue(new_id.charAt(i)) <= 9)|| (new_id.charAt(i) >= 'a' && new_id.charAt(i) <= 'z') || new_id.charAt(i) == '-' || new_id.charAt(i) == '_' || new_id.charAt(i) == '.')) {
                        checkStr = 1; break;
                    }
                    if (new_id.charAt(i) == '.') {
                        periodCheck++;
                    }
                    else periodCheck = 0;
                    if (periodCheck > 1) {
                        checkStr = 1;
                        break;
                    }
                }
            }
        }
        else checkStr = 1;
        if (checkStr == 1) { //형식에 틀렸으니, 단계별로 수정하는 로직.
            for (int i = 0; i < new_id.length(); i++) { //1~2단계
                if (new_id.charAt(i) >= 'A' && new_id.charAt(i) <= 'Z'){
                    char tmp = (char) (new_id.charAt(i)+32);
                    new_id = new_id.replace(new_id.charAt(i),tmp);
                }
                if (!((Character.getNumericValue(new_id.charAt(i)) >= 0 && Character.getNumericValue(new_id.charAt(i)) <= 9)|| (new_id.charAt(i) >= 'a' && new_id.charAt(i) <= 'z') || new_id.charAt(i) == '-' || new_id.charAt(i) == '_' || new_id.charAt(i) == '.')) {
                    new_id = strIndexRe(new_id,i); i--;
                }
            }
            int periodCheck = 0;
            if (new_id.length() > 1) {
                for (int i = 0; i < new_id.length(); i++) { //3단계
                    if (new_id.charAt(i) == '.') {
                        periodCheck++;
                    }
                    else periodCheck = 0;
                    if (periodCheck > 1) {
                        new_id = strIndexRe(new_id,i);
                        periodCheck--; i--;

                    }
                }
            }
            if (new_id.length() > 0 && new_id.charAt(0) == '.') {
                new_id = strIndexRe(new_id,0);
            }
            if (new_id.length() > 0 && new_id.charAt(new_id.length()-1) == '.') {
                new_id = strIndexRe(new_id,new_id.length()-1);
            }
            if (new_id.length() == 0) {
                new_id = "a";
            }
            if (new_id.length() >= 16) {
                String saveStr = "";
                for (int i = 0; i < 15; i++) {
                    saveStr += new_id.charAt(i);
                }
                new_id = saveStr;
            }
            if (new_id.length() > 1) {
                if (new_id.charAt(0) == '.') {
                    new_id = strIndexRe(new_id,0);
                }
                if (new_id.charAt(new_id.length()-1) == '.') {
                    new_id = strIndexRe(new_id,new_id.length()-1);
                }
            }
            if (new_id.length() <= 2) {
                while (true) {
                    new_id += new_id.charAt(new_id.length()-1);
                    if (new_id.length() == 3) break;
                }
            }
        }
        else return new_id;
        return new_id;
    }
    public static String strIndexRe(String str, int index) {
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            if (index != i) {
                result += str.charAt(i);
            }
        }
        return result;
    }
}
