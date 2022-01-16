from collections import deque
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = deque()
        for i in range(len(nums)):
            if nums[i] == 0: zeros.append(i)
            elif len(zeros) > 0:
                pop = zeros.popleft()
                nums[pop] = nums[i]
                nums[i] = 0
                zeros.append(i)
        return nums
