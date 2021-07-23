class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        last_end = intervals[0][1]
        result = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                result += 1
            else:
                last_end = intervals[i][1]
        return result
