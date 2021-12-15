class Solution:
    def totalNQueens(self, n: int) -> int:
        def myBackTrack(index1, index2, life):
            if life == 0:
                return 1
            if index1 >= n or index2 >= n:
                return 0
            sub_cnt = 0
            for i in range(n):
                if board[index1][i] == 0:
                    my_index = myBoardMark(index1, i)
                    sub_cnt += myBackTrack(index1 + 1, i, life - 1)
                    for value in my_index:
                        board[value[0]][value[1]] = 0
            return sub_cnt

        def myBoardMark(index1, index2):
            board[index1][index2] = -1
            my_index = [[index1, index2]]
            bias = 0
            for i in range(index1+1, n):
                bias += 1
                if board[i][index2] == 0:
                    my_index.append([i, index2])
                    board[i][index2] = -1
                if index2 - bias >= 0:
                    if board[i][index2 - bias] == 0:
                        my_index.append([i, index2 - bias])
                    board[i][index2 - bias] = -1
                if index2 + bias < n:
                    if board[i][index2 + bias] == 0:
                        my_index.append([i, index2 + bias])
                    board[i][index2 + bias] = -1
            return my_index

        result_cnt = 0
        for i in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            myBoardMark(0, i)
            sub_cnt = myBackTrack(1, i, n - 1)
            result_cnt += sub_cnt
        return result_cnt
