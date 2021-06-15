class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {int:int}
        for move in nums:
            if move in dict:
                dict[move] += 1
            else:
                dict[move] = 0
        for move in nums:
            if dict[move] == 0:
                return move
        return 1
        
