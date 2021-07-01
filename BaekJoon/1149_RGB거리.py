from sys import stdin

n = int(stdin.readline())

arr_cost = [list(map(int, stdin.readline().split())) for _ in range(n)]
memo_dict = {}

def dp_recursion(index, status_color):
    if index >= n:
        return 0
    global memo_dict
    key = str(index) + "|" + str(status_color)
    if key in memo_dict:
        return memo_dict[key]
    if status_color == 0:
        memo_dict[key] = min(dp_recursion(index+1, 1), dp_recursion(index+1, 2)) + arr_cost[index][status_color]
        return memo_dict[key]
    elif status_color == 1:
        memo_dict[key] = min(dp_recursion(index+1, 0), dp_recursion(index+1, 2)) + arr_cost[index][status_color]
        return memo_dict[key]
    elif status_color == 2:
        memo_dict[key] = min(dp_recursion(index+1, 0), dp_recursion(index+1, 1)) + arr_cost[index][status_color]
        return memo_dict[key]
      
print(min(dp_recursion(0, 0), dp_recursion(0, 1), dp_recursion(0, 2)))
