class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        crnt_n = 1
        while 3**crnt_n <= n:
            if 3**crnt_n == n:
                return True
            crnt_n += 1
        return False
