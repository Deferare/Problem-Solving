# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while True:
            mid = (left + right) // 2
            recive = guess(mid)
            if recive == 0:
                return mid
            elif recive == 1:
                left = mid + 1
            elif recive == -1:
                right = mid - 1
