class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for i in range(len(s)):
            if s[i] not in s_dict:
                if t[i] not in  t_dict:
                    s_dict[s[i]] = t[i]
                    t_dict[t[i]] = s[i]
                elif t_dict[t[i]] != s[i]:
                    return False
            elif s_dict[s[i]] != t[i]:
                return False
        return True
