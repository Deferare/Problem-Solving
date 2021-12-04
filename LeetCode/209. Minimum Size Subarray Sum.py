class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        check = 0
        min_len = len(nums)
        crnt_sum = 0
        first = 0
        for i in range(len(nums)):
            crnt_sum += nums[i]
            if crnt_sum >= target:
                check = 1
                while first <= i:
                    if crnt_sum >= target:
                        sub_len = i - first + 1
                        if sub_len < min_len:
                            min_len = sub_len
                    else:
                        break
                    crnt_sum -= nums[first]
                    first += 1
        if check == 0 and crnt_sum < target:
            return 0
        return min_len
