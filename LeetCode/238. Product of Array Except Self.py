class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return []
        zeros_s = set()
        accum = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_s.add(i)
            else:
                accum *= nums[i]
        if len(zeros_s) == 0:
            for i in range(len(nums)):
                if nums[i] < 0:
                    nums[i] = (accum//nums[i])
                else:
                    nums[i] = accum // nums[i]
        else:
            if len(zeros_s) == 1:
                for i in range(len(nums)):
                    if i in zeros_s: nums[i] = accum
                    else: nums[i] = 0
            else:
                for i in range(len(nums)):
                    nums[i] = 0
        return nums
