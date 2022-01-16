class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def cellCheck(ind_1, ind_2):
            cnt = 0
            for i in range(ind_1 - 1, ind_1 + 2):
                if i < 0 or i >= len(board): continue
                for j in range(ind_2 - 1, ind_2 + 2):
                    if j < 0 or j >= len(board[0]): continue
                    if i == ind_1 and j == ind_2: continue
                    if board[i][j] == 1: cnt += 1
            return cnt
        def gameStart(ind_1, ind_2):
            if ind_2 >= len(board[0]):
                ind_1 += 1
                ind_2 = 0
            if ind_1 >= len(board): return
            check = cellCheck(ind_1, ind_2)
            gameStart(ind_1, ind_2 + 1)
            if check < 2 or check > 3: board[ind_1][ind_2] = 0
            elif check >= 2 and check <= 3 and board[ind_1][ind_2] == 1: pass
            elif check == 3: board[ind_1][ind_2] = 1
        gameStart(0, 0)
        return board
