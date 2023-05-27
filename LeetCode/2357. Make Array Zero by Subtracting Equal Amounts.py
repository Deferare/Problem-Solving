class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        answer = len(s)
        if 0 in s:
            return answer - 1
        return answer
