class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        x_maxs = []
        y_maxs = []
        for i in range(len(grid)):
            x_max = 0
            y_max = 0
            for j in range(len(grid[0])):
                if grid[i][j] > y_max: y_max = grid[i][j]
                if grid[j][i] > x_max: x_max = grid[j][i]
            x_maxs.append(x_max)
            y_maxs.append(y_max)
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer += min(x_maxs[j], y_maxs[i]) - grid[i][j]
        return answer
