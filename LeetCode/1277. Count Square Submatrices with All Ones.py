class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dplist = [[0] * (len(matrix[0])) for i in range(len(matrix))]
        for i in range(0,len(matrix[0])):
            dplist[0][i] = matrix[0][i]
        for i in range(0, len(matrix)):
            dplist[i][0] = matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    dplist[i][j] = 0
                    continue
                value = min(dplist[i-1][j],dplist[i-1][j-1], dplist[i][j-1]) + 1
                dplist[i][j] = value
        sum = 0
        for i in range(0, len(dplist)):
            for j in range(0,len(dplist[0])):
               sum += dplist[i][j]
        return sum
        
