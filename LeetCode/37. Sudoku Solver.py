class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def sudoku(crnt_board, index1, index2):
            if index1 < 8 and index2 > 8:
                return sudoku(crnt_board, index1 + 1, 0)
            if index1 > 8 or index2 > 8:
                for i in range(9):
                    for j in range(9):
                        if crnt_board[i][j] == ".":
                            return False
                return True
            if crnt_board[index1][index2] != ".":
                return sudoku(crnt_board, index1, index2 + 1)
            for value in range(1, 10):
                value = str(value)
                if isvalid(crnt_board, value, index1, index2):
                    crnt_board[index1][index2] = value
                    if sudoku(crnt_board, index1, index2 + 1):
                        return True
                    else:
                        crnt_board[index1][index2] = "."
            return False

        def isvalid(crnt_board, crnt_value, i, j):
            index1 = (i // 3) * 3
            index2 = (j // 3) * 3
            for i_1 in range(index1, index1 + 3):
                for j_1 in range(index2, index2 + 3):
                    if crnt_value == crnt_board[i_1][j_1]:
                        return False
            for i_1 in range(9):
                if crnt_value == crnt_board[i][i_1]:
                    return False
                if crnt_value == crnt_board[i_1][j]:
                    return False
            return True
        sudoku(board, 0, 0)
