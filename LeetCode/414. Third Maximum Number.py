class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dict_my = dict()
        for i in range(len(nums)):
            if nums[i] not in dict_my:
                dict_my[nums[i]] = 1
            else:
                dict_my[nums[i]] += 1
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(dict_my) > 2:
            return nums[2]
        return nums[0]
