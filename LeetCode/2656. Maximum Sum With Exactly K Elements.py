class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        answer = 0
        for _ in range(k):
            answer += max_num
            max_num += 1
        return answer
