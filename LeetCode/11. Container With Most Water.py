class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result = 0
        while start < end:
            crnt = end - start
            if height[start] < height[end]:
                crnt *= height[start]
                start += 1
            else:
                crnt *= height[end]
                end -= 1
            if crnt > result: result = crnt
        return result
