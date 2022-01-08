class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split_into_pieces(mid):
            previous_sum = 0
            pieces = 1
            for i in range(len(nums)):
                previous_sum += nums[i]
                if previous_sum > mid:
                    previous_sum = nums[i]
                    pieces += 1
            return pieces
        start = max(nums)
        end = sum(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            pieces = split_into_pieces(mid)
            if pieces > m:
                start = mid + 1
            else:
                end = mid
        if split_into_pieces(start) <= m:
            return start
        return end
