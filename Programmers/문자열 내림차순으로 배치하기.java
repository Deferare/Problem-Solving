class Solution {
    public String solution(String s) {
        String small = ""; String big = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < 91) {
                small += s.charAt(i);
            }
            else if (s.charAt(i) > 96) {
                big += s.charAt(i);
            }
        }
        char[] smallC = new char[small.length()];
        for (int i = 0; i < smallC.length; i++) {
            smallC[i] = small.charAt(i);
        }
        for (int i = 0; i < smallC.length-1; i++) {
            for (int j = 0; j < smallC.length-1; j++) {
                if (Character.getNumericValue(smallC[j]) < Character.getNumericValue(smallC[j+1])) {
                    char a = smallC[j]; char b = smallC[j+1];
                    smallC[j] = b;
                    smallC[j+1] = a;
                }
            }
        }
        char[] bigC = new char[big.length()];
        for (int i = 0; i < bigC.length; i++) {
            bigC[i] = big.charAt(i);
        }
        for (int i = 0; i < bigC.length-1; i++) {
            for (int j = 0; j < bigC.length-1; j++) {
                if (Character.getNumericValue(bigC[j]) < Character.getNumericValue(bigC[j+1])) {
                    char a = bigC[j]; char b = bigC[j+1];
                    bigC[j] = b;
                    bigC[j+1] = a;
                }
            }
        }
        String result = "";
        for (int i = 0; i < bigC.length; i++) {
            result += bigC[i];
        }
        for (int i = 0; i < smallC.length; i++) {
            result += smallC[i];
        }
        return result;
    }
}
