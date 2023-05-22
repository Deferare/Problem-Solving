class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = [0]*(len(citations)+1)
        for i in range(0, len(citations)):
            if citations[i] >= len(arr):
                arr[-1] += 1
            else:
                arr[citations[i]] += 1
        accrued = 0
        for i in range(0, len(arr)).__reversed__():
            accrued += arr[i]
            if i <= accrued: return i
        return 0
