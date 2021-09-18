def solution(board, moves):
    result_cnt = 0
    stack = []
    clear = set()
    for order in moves:
        if order not in clear:
            check = 0
            for i in range(len(board)):
                if board[i][order-1] != 0:
                    push = board[i][order-1]
                    board[i][order - 1] = 0
                    if len(stack) > 0 and stack[-1] == push:
                        stack.pop()
                        result_cnt += 2
                    else:
                        stack.append(push)
                    check = 1
                    break
            if check == 0:
                clear.add(order)
    return result_cnt
