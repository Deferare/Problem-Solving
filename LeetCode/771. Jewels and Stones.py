class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        result_cnt = 0
        for crnt in stones:
            if crnt in jewels_set:
                result_cnt += 1
        return result_cnt
