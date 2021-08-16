class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1
