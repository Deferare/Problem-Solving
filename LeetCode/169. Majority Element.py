class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {int:int}
        max = 0
        result = nums[0]
        for move in nums:
            if move in dict:
                dict[move] += 1
                if dict[move] > max:
                    max = dict[move]
                    result = move
            else:
                dict[move] = 1
        return result
        
