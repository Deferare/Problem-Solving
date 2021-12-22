class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def update(index_1, index_2):
            for i in range(len(matrix)):
                matrix[i][index_2] = 0
            for i in range(len(matrix[0])):
                matrix[index_1][i] = 0
        zero_indexs = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_indexs.append([i, j])
        for i in range(len(zero_indexs)):
            index = zero_indexs[i]
            update(index[0], index[1])
