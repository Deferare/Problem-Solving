from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        counts = Counter()
        counts[-nums[0]] += 1
        counts[nums[0]] += 1
        for num in nums[1:]:
            new = Counter()
            for key in counts.keys():
                new[key + num] += counts[key]
                new[key - num] += counts[key]
            counts = new
        return counts[S]
