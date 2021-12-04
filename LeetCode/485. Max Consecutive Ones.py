class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result_max = 0
        crnt_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                crnt_max += 1
                if crnt_max > result_max:
                    result_max = crnt_max
            else:
                crnt_max = 0
        return result_max
