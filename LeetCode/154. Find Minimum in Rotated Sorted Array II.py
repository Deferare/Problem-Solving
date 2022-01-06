class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(left, right):
            if left >= right:
                return nums[left]
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            return min(nums[left], nums[right], binarySearch(left + 1, mid), binarySearch(mid + 1, right - 1))
        return binarySearch(0, len(nums) - 1)
