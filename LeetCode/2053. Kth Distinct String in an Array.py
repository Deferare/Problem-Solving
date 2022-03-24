class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = dict()
        for c in arr:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        ktCheck = 0
        for i in range(len(arr)):
            if dic[arr[i]] == 1:
                ktCheck += 1
                if ktCheck == k:
                    return arr[i]
        return ""
