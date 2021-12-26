class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_n = -200000
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
                if nums[i] > max_n:
                    max_n = nums[i]
            else:
                d[nums[i]] += 1
        k_check = 0
        for num in range(-200000, max_n+1).__reversed__():
            if num in d:
                k_check += d[num]
                if k_check >= k:
                    return num
        return max_n
