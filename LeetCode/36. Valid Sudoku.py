class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col_set = set()
            row_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in col_set:
                        return False
                    else:
                        col_set.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in row_set:
                        return False
                    else:
                        row_set.add(board[j][i])
                if i%3 == 0 and j%3 == 0:
                    matrix_set = set()
                    for i_1 in range(i, i+3):
                        for j_1 in range(j, j + 3):
                            if board[i_1][j_1] != ".":
                                if board[i_1][j_1] in matrix_set:
                                    return False
                                else:
                                    matrix_set.add(board[i_1][j_1])
        return True
