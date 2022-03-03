class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            check = 1
            for j in range(len(words[i])//2):
                if words[i][j] != words[i][-(j+1)]:
                    check = 0
                    break
            if check:
                return words[i]
        return ""
