class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [nums[0]]
        right_sum = [nums[-1]]
        for i in range(1, n):
            left_sum.append(left_sum[i-1] + nums[i])
            right_sum.append(right_sum[i-1] + nums[-i-1])
        for i in range(n):
            left_sum[i] = abs(left_sum[i] - right_sum[-i-1])
        return left_sum
