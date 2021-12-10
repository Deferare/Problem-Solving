from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def update(index_1, index_2, pre_v):
            if index_1 < 0 or index_2 < 0 or index_1 >= n or index_2 >= m:
                return
            if result_mat[index_1][index_2] == -1:
                result_mat[index_1][index_2] = pre_v + 1
                q.append([index_1, index_2])
            else:
                if result_mat[index_1][index_2] > pre_v + 1:
                    result_mat[index_1][index_2] = pre_v + 1
                    q.append([index_1, index_2])
        n = len(mat)
        m = len(mat[0])
        result_mat = [list(-1 for _ in range(m)) for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append([i,j])
                    result_mat[i][j] = 0
        while len(q) > 0:
            pop = q.popleft()
            update(pop[0] + 1, pop[1], result_mat[pop[0]][pop[1]])
            update(pop[0], pop[1] + 1, result_mat[pop[0]][pop[1]])
            update(pop[0] - 1, pop[1], result_mat[pop[0]][pop[1]])
            update(pop[0], pop[1] - 1, result_mat[pop[0]][pop[1]])

        return result_mat
