class Solution:
    def getMaxLen(self, nums):
        start = None
        nag_end = None
        nag_cnt = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                start = None
                nag_end = None
                nag_cnt = 0
            else:
                if start == None: start = i
                if nums[i] < 0: nag_cnt += 1
                if nag_cnt%2 == 0:
                    result = max(result, i - start + 1)
                elif nag_end == None:
                    nag_end = i
                else:
                    result = max(result, i - nag_end)
        return result
