class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        cnt = 0
        for i in range(len(n)):
            if n[i] == "1":
                cnt += 1
        return cnt
