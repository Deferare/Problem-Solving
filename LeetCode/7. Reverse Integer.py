class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        result = ""
        if x[0] == "-":
            result += "-"
            for i in range(1, len(x)).__reversed__():
                result += x[i]
        else:
            for i in range(len(x)).__reversed__():
                result += x[i]
        result = int(result)
        if result > 2**31 or result < -2**31:
            return 0
        return str(result)
