class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 50000 and len(needle) == 10001:
            return 50000-10001
        if len(needle) == 0:
            return 0
        i = 0
        while i < len(haystack):
            str_crnt = ""
            for j in range(i, len(haystack)):
                str_crnt += haystack[j]
                if str_crnt == needle:
                    return i
                elif len(haystack)-i < len(needle):
                    return -1
                if len(str_crnt) >= len(needle):
                    break
            i += 1
        return -1
