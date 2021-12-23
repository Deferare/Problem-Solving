class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i, l = 0, 0
        for j in range(len(s)):
            s_1 = s[j-l: j+1]
            if s_1 == s_1[::-1]:
                i = j - l
                l += 1
            else:
                s_2 = s[j - l - 1: j + 1]
                if j > l and s_2 == s_2[::-1]:
                    i = j - l - 1
                    l += 2
        return s[i: i+l]
