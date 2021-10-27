class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ""
        for i in range(len(num)).__reversed__():
            if int(num[i])%2 != 0:
                result = num[:i+1]
                break
        return result
        
