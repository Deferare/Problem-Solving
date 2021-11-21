from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0:
            return False
        q = deque([nums[0]])
        s = set()
        s.add(nums[0])
        for i in range(1, len(nums)):
            if nums[i] in s:
                return True
            if len(q) == k:
                s.remove(q.popleft())
            q.append(nums[i])
            s.add(nums[i])
        return False
        
