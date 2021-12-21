class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            crnt = abs(nums[i])
            if crnt <= len(nums):
                nums[crnt-1] = -abs(nums[crnt-1])
        result = []
        for i in range(len_nums):
            if nums[i] > 0:
                result.append(i+1)
        return result
