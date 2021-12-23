class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        one = nums[0]
        two = 5000000000
        for i in range(1, len(nums)):
            if nums[i] > two:
                return True
            elif nums[i] > one:
                two = nums[i]
            elif nums[i] < one:
                one = nums[i]
        return False
