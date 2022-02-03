class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0": return 0
        N = len(s)
        result, pre2, pre = 1, 1, 1
        for i in range(1, N):
            if s[i] == "0":
                if s[i-1] != "1" and s[i-1] != "2": return 0
                elif i > 1:
                    num2 = int(s[i - 2] + s[i - 1])
                    if num2 > 10 and num2 <= 26:
                        result = pre2
                        pre = pre2
            else:
                num = int(s[i-1] + s[i])
                if num >= 10 and num <= 26:
                    if i > 1:
                        num2 = int(s[i - 2] + s[i - 1])
                        if num2 > 10 and num2 <= 26:
                            result = pre2 + pre
                            pre2 = pre
                            pre = result
                            continue
                    result += pre
                    pre2 = pre
                    pre = result
        return result
