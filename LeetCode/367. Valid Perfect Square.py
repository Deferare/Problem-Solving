class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        n = 2
        pre_n = n
        while n * n <= num:
            sqr = n * n
            if sqr == num:
                return True
            pre_n = n
            n = sqr
        while pre_n*pre_n <= num:
            crnt = pre_n * pre_n
            if crnt == num:
                return True
            pre_n += 1
        return False
