class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]
        result = []
        index_1 = 0
        index_2 = 0
        turn = 0
        while True:
            if matrix[index_1][index_2] == -1000:
                break
            result.append(matrix[index_1][index_2])
            matrix[index_1][index_2] = -1000
            if turn == 0:
                if index_2+1 >= len(matrix[0]) or matrix[index_1][index_2+1] == -1000:
                    index_1 += 1
                    turn = 1
                else:
                    index_2 += 1
            elif turn == 1:
                if index_1+1 >= len(matrix) or matrix[index_1+1][index_2] == -1000:
                    index_2 -= 1
                    turn = 2
                else:
                    index_1 += 1
            elif turn == 2:
                if index_2-1 < 0 or matrix[index_1][index_2-1] == -1000:
                    index_1 -= 1
                    turn = 3
                else:
                    index_2 -= 1
            elif turn == 3:
                if index_1 - 1 < 0 or matrix[index_1-1][index_2] == -1000:
                    index_2 += 1
                    turn = 0
                else:
                    index_1 -= 1
        return result
