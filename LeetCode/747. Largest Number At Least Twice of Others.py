class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ele_1 = 0
        ele_2 = 0
        index_2 = 0
        for i in range(len(nums)):
            if nums[i] > ele_2:
                ele_1 = ele_2
                ele_2 = nums[i]
                index_2 = i
            elif nums[i] > ele_1:
                ele_1 = nums[i]
        if ele_1*2 > ele_2:
            return -1
        return index_2
