class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_crnt = dict()
        max_check = 0
        for i in range(len(s)):
            if s[i] not in dict_crnt:
                dict_crnt[s[i]] = i
                if len(dict_crnt) > max_check:
                    max_check = len(dict_crnt)
            else:
                dict_new = dict()
                index = dict_crnt[s[i]]
                for j in range(index, i+1):
                    dict_new[s[j]] = j
                dict_crnt = dict_new
        return max_check
