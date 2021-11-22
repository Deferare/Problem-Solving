class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result_cnt = 1
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                result_cnt += 1
                nums[index] = nums[i]
                index += 1
        for _ in range(index, len(nums)).__reversed__():
            nums.pop()
        return result_cnt
