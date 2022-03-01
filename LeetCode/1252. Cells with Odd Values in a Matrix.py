class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [list(0 for _ in range(n)) for _ in range(m)]
        for i in range(len(indices)):
            for j in range(m):
                matrix[j][indices[i][1]] += 1
            for j in range(n):
                matrix[indices[i][0]][j] += 1
        cnt = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2 != 0: cnt += 1
        return cnt
