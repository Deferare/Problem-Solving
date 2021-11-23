class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_convert = ""
        for i in range(len(s)):
            crnt_asci = ord(s[i])
            if crnt_asci >= 65 and crnt_asci <= 90:
                str_convert += chr(crnt_asci+32)
            elif (crnt_asci >= 97 and crnt_asci <= 122) or (crnt_asci >= 48 and crnt_asci <= 57):
                str_convert += chr(crnt_asci)
        for i in range(len(str_convert)//2):
            if str_convert[i] != str_convert[len(str_convert)-1-i]:
                return False
        return True
