class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = -1
        for i in range(len(nums)-1).__reversed__():
            for j in range(i + 1, i + nums[i] + 1):
                if nums[j] == -1:
                    nums[i] = -1
                    break
        if nums[0] == -1:
            return True
        return False
