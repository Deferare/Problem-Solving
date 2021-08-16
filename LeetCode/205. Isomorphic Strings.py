class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        save_dict_1 = {}
        save_dict_2 = {}
        for i in range(len(s)):
            if s[i] not in save_dict_1:
                if t[i] not in save_dict_2:
                    save_dict_1[s[i]] = t[i]
                    save_dict_2[t[i]] = s[i]
                else:
                    if save_dict_2[t[i]] != s[i]:
                        return False
            else:
                if save_dict_1[s[i]] != t[i]:
                    return False
        return True
