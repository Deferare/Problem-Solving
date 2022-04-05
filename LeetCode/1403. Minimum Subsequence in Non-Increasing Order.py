class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse= True)
        amount = sum(nums)
        answer = []
        crnt_sum = 0
        for n in nums:
            answer.append(n)
            crnt_sum += n
            amount -= n
            if crnt_sum > amount: break
        return answer
