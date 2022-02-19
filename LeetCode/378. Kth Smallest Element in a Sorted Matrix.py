class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        n_min = matrix[0][0]
        n_max = matrix[-1][-1]
        while n_min <= n_max:
            n_mid = (n_min + n_max)//2
            cnt = 0
            for i in range(N):
                for j in range(N):
                    if matrix[i][0] > n_mid: break
                    if matrix[i][j] <= n_mid: cnt += 1
            if cnt < k: n_min = n_mid + 1
            else: n_max = n_mid - 1
        return n_min
