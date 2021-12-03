class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        index_1 = 0
        index_2 = 0
        turn = 1
        while True:
            result.append(mat[index_1][index_2])
            if index_1 == len(mat)-1 and index_2 == len(mat[0])-1:
                break
            if turn == 1:
                if index_1-1 >= 0 and index_2+1 < len(mat[0]):
                    index_1 -= 1
                    index_2 += 1
                else:
                    if index_2+1 < len(mat[0]):
                        index_2 += 1
                    else:
                        index_1 += 1
                    turn = 0
            elif turn == 0:
                if index_1+1 < len(mat) and index_2-1 >= 0:
                    index_1 += 1
                    index_2 -= 1
                else:
                    if index_1+1 < len(mat):
                        index_1 += 1
                    else:
                        index_2 += 1
                    turn = 1
        return result
