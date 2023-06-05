class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count_parentheses = 0
        for i in range(len(s)):
            if s[i] == "(":
                count_parentheses += 1
                max_count = max(max_count, count_parentheses)
            elif s[i] == ")": count_parentheses -= 1
        return max_count
