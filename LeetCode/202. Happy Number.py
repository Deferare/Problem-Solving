class Solution:
    def isHappy(self, n: int) -> bool:
        overlab_check = set()
        while n != 1:
            n_str = str(n)
            sum = 0
            for i in range(len(n_str)):
                sum += int(n_str[i])**2
            if sum in overlab_check:
                return False
            n = sum
            overlab_check.add(n)
        return True
