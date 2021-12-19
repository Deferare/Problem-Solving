class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        left = [1]
        stack = [[heights[0], 1]]
        for i in range(1, len_heights):
            crnt_left = 1
            if heights[i] <= stack[-1][0]:
                while len(stack) > 0:
                    pop = stack.pop()
                    if pop[0] < heights[i]:
                        stack.append(pop)
                        break
                    crnt_left += pop[1]
            stack.append([heights[i], crnt_left])
            left.append(crnt_left)
        right = [1]
        stack = [[heights[-1], 1]]
        for i in range(0, len_heights-1).__reversed__():
            crnt_right = 1
            if heights[i] <= stack[-1][0]:
                while len(stack) > 0:
                    pop = stack.pop()
                    if pop[0] < heights[i]:
                        stack.append(pop)
                        break
                    crnt_right += pop[1]
            stack.append([heights[i], crnt_right])
            right.append(crnt_right)
        result_max = 0
        for i in range(len_heights):
            crnt = heights[i] * (left[i] + right[-(i+1)] - 1)
            if crnt > result_max:
                result_max = crnt
        return result_max
