class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        result_arr = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result_arr[-1][1]:
                if intervals[i][1] > result_arr[-1][1]:
                    result_arr[-1][1] = intervals[i][1]
            else:
                result_arr.append(intervals[i].copy())
        return result_arr
