class Solution:
    def countOdds(self, low: int, high: int) -> int:
        value = (high - low)//2
        if low%2 != 0 or high%2 != 0: value += 1
        return value
