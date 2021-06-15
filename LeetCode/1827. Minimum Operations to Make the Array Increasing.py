from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max = nums[0]
        result = 0
        for i in range(1,len(nums)):
            if nums[i] <= max:
                save = max-nums[i]+1
                result += save
                max = nums[i] + save
            elif nums[i] > max:
                max = nums[i]
        return result
