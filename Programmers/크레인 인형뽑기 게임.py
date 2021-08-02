def solution(board, moves):
    board_len = len(board)
    board_dict = {}
    for i in range(board_len):
        sub_arr = []
        for j in range(1, board_len+1):
            if board[-j][i] != 0:
                sub_arr.append(board[-j][i])
            else:
                break
        board_dict[i+1] = sub_arr
    answer = 0
    basket_arr = []
    for crnt in moves:
        if len(basket_arr) == 0:
            if len(board_dict[crnt]) != 0:
                basket_arr.append(board_dict[crnt].pop())
        else:
            if len(board_dict[crnt]) != 0:
                if basket_arr[-1] == board_dict[crnt][-1]:
                    basket_arr.pop()
                    board_dict[crnt].pop()
                    answer += 2
                else:
                    basket_arr.append(board_dict[crnt].pop())
    return answer
