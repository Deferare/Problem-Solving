class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        arr = nums[len(nums)-k:]
        for i in range(len(nums)-k).__reversed__():
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = arr[i]
