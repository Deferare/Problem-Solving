class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(start, end):
            if start >= end:
                return start
            mid = start + ((end-start)//2)
            index = mid
            if nums[mid] < target:
                index = findIndex(mid+1, end)
            elif nums[mid] > target:
                index = findIndex(start, mid)
            return index
        index = findIndex(0, len(nums)-1)
        if len(nums) == 0 or nums[index] != target:
            return [-1, -1]
        while index >= 0:
            if nums[index] != target:
                break
            index -= 1
        index += 1
        index_2 = index
        while index_2 < len(nums):
            if nums[index_2] != target:
                break
            index_2 += 1
        return [index, index_2-1]
