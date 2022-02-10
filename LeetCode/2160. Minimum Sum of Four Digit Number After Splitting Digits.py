class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        arr = []
        for i in range(len(s)):
            if s[i] != "0": arr.append(s[i])
        arr.sort()
        N = len(arr)
        if N == 4: return int(arr[0]+arr[2]) + int(arr[1]+arr[3])
        elif N == 3: return int(arr[0] + arr[1]) + int(arr[2])
        elif N == 2: return int(arr[0]) + int(arr[1])
        elif N == 1: return int(arr[0])
        elif N == 0: return 0
