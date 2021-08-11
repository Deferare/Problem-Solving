class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result_arr = []
        for crnt in nums:
            result_arr.append(nums[crnt])
        return result_arr
