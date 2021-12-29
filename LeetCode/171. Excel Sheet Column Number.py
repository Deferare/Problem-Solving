class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        bias = 1
        for i in range(len(columnTitle)).__reversed__():
            value = (ord(columnTitle[i]) - 64)
            if bias != 0:
                value = (ord(columnTitle[i])-64) * bias
            result += value
            bias *= 26
        return result
