class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dp(start, end):
            accum = 0
            crnt = 0
            for i in range(start, end):
                tmp = max(accum, crnt)
                accum = max(nums[i], crnt + nums[i])
                crnt = tmp
            return max(accum, crnt)
        return max(dp(1, len(nums)), dp(0, len(nums) - 1))
