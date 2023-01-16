class Solution:
    def integerReplacement(self, n: int) -> int:
        counted = 0
        while True:
            if n == 1:
                break
            elif n == 3:
                counted += 2
                break
            if n%2 == 0:
                n //= 2
            elif ((n-1)//2)%2 != 0:
                n += 1
            else:
                n -= 1
            counted += 1

        return counted
