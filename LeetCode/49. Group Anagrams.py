class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in range(len(strs)):
            crnt_str = [crnt for crnt in strs[i]]
            crnt_str.sort()
            crnt_str_2 = ""
            for j in range(len(crnt_str)):
                crnt_str_2 += crnt_str[j]
            if crnt_str_2 not in d:
                d[crnt_str_2] = [strs[i]]
            else:
                d[crnt_str_2].append(strs[i])
        result = []
        for value in d.values():
            result.append(value)
        return result
        
