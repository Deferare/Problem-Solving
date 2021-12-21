from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        q = deque()
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and len(q) > 0:
                pop = q.popleft()
                tmp = nums[pop]
                nums[pop] = nums[i]
                nums[i] = tmp
                q.append(i)
            elif nums[i] % 2 != 0:
                q.append(i)
        return nums
