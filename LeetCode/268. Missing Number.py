class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        memo_dict = {nums[i]:1 for i in range(nums_len)}
        for i in range(nums_len+1):
            if i not in memo_dict:
                return i
