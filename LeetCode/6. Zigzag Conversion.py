class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        board = [""] * numRows
        row = direction = 0
        for c in s:
            board[row] += c
            if row == 0:
                direction = 1
            elif row == numRows-1:
                direction = -1
            row += direction

        return "".join(board)
