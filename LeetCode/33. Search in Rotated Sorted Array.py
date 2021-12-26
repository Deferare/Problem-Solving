class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def myBoth(start, end):
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            if start == end:
                return -1
            if nums[start] < nums[end] and (target > nums[end] or target < nums[start]):
                return -1
            left = myBoth(start, mid)
            if left == -1:
                right = myBoth(mid+1, end)
                if right == -1:
                    return -1
                else:
                    return right
            else:
                return left
            return -1
        return myBoth(0, len(nums)-1)
