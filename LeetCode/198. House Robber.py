class Solution:
    def rob(self, nums: List[int]) -> int:
        pre_1 = 0
        pre_2 = 0
        for i in range(len(nums)):
            crnt = max(pre_2, pre_1+nums[i])
            pre_1 = pre_2
            pre_2 = crnt
        return pre_2
