class Solution:
    def jump(self, nums: List[int]) -> int:
        arr = [10000 for _ in range(len(nums))]
        arr[0] = 0
        for i in range(len(nums)):
            for j in range(i, i + nums[i] + 1):
                if j < len(nums):
                    if arr[j] > arr[i] + 1:
                        arr[j] = arr[i] + 1
        return arr[-1]
