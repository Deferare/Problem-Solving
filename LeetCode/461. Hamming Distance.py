class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = format(x, "032b")
        y = format(y, "032b")
        cnt = 0
        for i in range(32):
            if x[i] != y[i]:
                cnt += 1
        return cnt
