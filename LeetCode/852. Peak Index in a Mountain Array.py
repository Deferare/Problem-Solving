class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        pre_number = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < pre_number:
                return i-1
            else:
                pre_number = arr[i]
        return pre_number
