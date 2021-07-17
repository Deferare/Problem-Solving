from sys import stdin

n,m = map(int, stdin.readline().split(" "))
n_dict = {stdin.readline().strip():1 for _ in range(n)}
result_check = 0
for _ in range(m):
    if stdin.readline().strip() in n_dict:
        result_check += 1
        
print(result_check)
