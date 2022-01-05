min_n = 5001
class Solution:
    def findMin(self, nums: List[int]) -> int:
        global min_n
        def binarySearch(left, right):
            if left > right:
                return
            global min_n
            if nums[left] < nums[right]:
                if nums[left] < min_n:
                    min_n = nums[left]
                return
            mid = (left + right) // 2
            if nums[left] < min_n:
                min_n = nums[left]
            if nums[right] < min_n:
                min_n = nums[right]
            if nums[mid] < min_n:
                min_n = nums[mid]
            binarySearch(left + 1, mid)
            binarySearch(mid, right - 1)
        min_n = 5001
        binarySearch(0, len(nums) - 1)
        return min_n
