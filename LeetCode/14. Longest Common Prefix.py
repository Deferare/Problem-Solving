class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return result
                if strs[0][i] != strs[j][i]:
                    return result
            if len(strs[0]) > i:
                result += strs[0][i]
            else:
                break
        return result
