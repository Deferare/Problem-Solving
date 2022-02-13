class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums = list(nums_set)
        N = len(nums)
        result = 0
        for i in range(N):
            if nums[i] - 1 in nums_set:
                continue
            tmp = nums[i]
            crnt_len = 1
            while tmp + crnt_len in nums_set:
                crnt_len += 1
            if crnt_len > result: result = crnt_len
        return result
