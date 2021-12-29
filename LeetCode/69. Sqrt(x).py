class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = int(left + ((right-left)/2))
            if (x/mid) < mid:
                right = mid - 1
            elif (x/mid) > mid:
                left = mid + 1
            else:
                return int(mid)
        return left-1
