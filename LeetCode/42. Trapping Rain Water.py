class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        crnt = 0
        stack = []
        while crnt < len(height):
            while len(stack) != 0 and height[crnt] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if len(stack) == 0: break
                distance = crnt - stack[-1] - 1
                bounded_height = min(height[crnt], height[stack[-1]]) - height[top]
                answer += (distance * bounded_height)
            stack.append(crnt)
            crnt += 1
        return answer
