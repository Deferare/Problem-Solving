class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        crnt_min = nums[0]
        for i in range(len(nums)):
            if (nums[i] - crnt_min) > k:
                count += 1
                crnt_min = nums[i]
        return count
