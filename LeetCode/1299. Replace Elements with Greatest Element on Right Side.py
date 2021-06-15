from typing import List
class Solution:
    def replaceElements(self,arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        result:[int] = [0] * len(arr)
        max = -1
        for i in range(len(arr)-1, -1,-1):
            result[i] = max
            if arr[i] > max:
                max = arr[i]
        return result
        
