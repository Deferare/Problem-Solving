class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = nums[0]+nums[-1]
        for i in range(len(nums)//2):
            crnt = nums[i] + nums[-(i+1)]
            answer = max(answer, crnt)
        return answer
