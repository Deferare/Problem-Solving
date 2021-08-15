class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n = n
        while n > 1:
            if n%2 == 0:
                n //= 2
            else:
                break
        if n == 1:
            return True
        else:
            return False
