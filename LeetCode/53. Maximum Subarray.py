class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_check = nums[0]
        crnt_sum = nums[0]
        for i in range(1, len(nums)):
            a = crnt_sum + nums[i]
            if a > nums[i]:
                crnt_sum = a
            else:
                crnt_sum = nums[i]
            if crnt_sum > max_check:
                max_check = crnt_sum
        return max_check
