class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        made_str = []
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                made_str.append(min(s[i], s[-i-1]))
            else:
                made_str.append(s[i])
        return "".join(made_str)
