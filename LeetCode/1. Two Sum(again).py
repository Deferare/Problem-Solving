class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]
        nums.sort()
        bottom_index = 0
        top_index = len(nums)-1
        while bottom_index < top_index:
            sub_sum = nums[bottom_index]+nums[top_index]
            if sub_sum == target:
                if nums[bottom_index] == nums[top_index]:
                    return [nums_dict[nums[bottom_index]][0], nums_dict[nums[top_index]][1]]
                return [nums_dict[nums[bottom_index]][0], nums_dict[nums[top_index]][0]]
            if sub_sum < target:
                bottom_index += 1
            else:
                top_index -= 1
        return [nums_dict[nums[bottom_index]][0], nums_dict[nums[top_index]][1]]
