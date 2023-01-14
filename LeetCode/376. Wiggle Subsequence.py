class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        answer_1 = 1
        answer_2 = 1
        state_1 = True
        state_2 = False
        lastV_1 = nums[0]
        lastV_2 = nums[0]
        for i in range(1, length):
            crnt_1 = nums[i]
            if state_1 == True:
                if crnt_1 > lastV_1:
                    answer_1 += 1
                    state_1 = False
                lastV_1 = crnt_1
            else:
                if crnt_1 < lastV_1:
                    answer_1 += 1
                    state_1 = True
                lastV_1 = crnt_1
            crnt_2 = nums[i]
            if state_2 == True:
                if crnt_2 > lastV_2:
                    answer_2 += 1
                    state_2 = False
                lastV_2 = crnt_2
            else:
                if crnt_2 < lastV_2:
                    answer_2 += 1
                    state_2 = True
                lastV_2 = crnt_2
        return max(answer_1, answer_2)
