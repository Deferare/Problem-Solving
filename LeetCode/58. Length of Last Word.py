class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0
        crnt_str = ""
        for i in range(len(s)).__reversed__():
            if s[i] != " ":
                crnt_str += s[i]
            elif crnt_str != "": break
        word_len = len(crnt_str)
        return word_len
