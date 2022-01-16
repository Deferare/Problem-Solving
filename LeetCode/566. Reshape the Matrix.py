class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if r*c != n*m: return mat
        mat_new = []
        crnt = []
        for i in range(n):
            for j in range(m):
                crnt.append(mat[i][j])
                if len(crnt) == c:
                    mat_new.append(crnt.copy())
                    crnt = []
        return mat_new
