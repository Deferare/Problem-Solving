from collections import deque
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = deque()
        cnt = 0
        first = 0
        second = 0
        while second < len(nums):
            if nums[first] != -1 and len(q) > 0:
                first = q.popleft()
            if nums[second] != val:
                if nums[first] == -1:
                    nums[first] = nums[second]
                    nums[second] = -1
                    q.append(second)
                cnt += 1
            else:
                nums[second] = -1
                q.append(second)
            if nums[first] != -1 and len(q) > 0:
                first = q.popleft()
            second += 1
        return cnt
