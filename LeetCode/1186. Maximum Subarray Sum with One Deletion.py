class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        result = arr[0]
        max_1 = arr[0]
        max_2 = arr[0]
        for i in range(1, len(arr)):
            crnt = max(arr[i], max_1+arr[i])
            max_2 = max(max_2+arr[i], max_1)
            max_1 = crnt
            if max_1 > result:
                result = max_1
            if max_2 > result:
                result = max_2
        return result
