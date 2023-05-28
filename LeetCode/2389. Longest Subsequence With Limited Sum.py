class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])
        answer = []
        for q in queries:
            index = bisect.bisect_right(prefix_sum, q)
            answer.append(index)
        return answer
