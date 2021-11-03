from sys import stdin
def my_bfs(x,y):
    global visited, next, matrix
    if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] != -1:
        return
    visited[x][y] = 1
    if matrix[x][y] == "0":
        matrix[x][y] = "1"
    if matrix[x][y] == "1":
        next.append([x, y])
        
n,m = map(int, stdin.readline().split(" "))
visited = [list(-1 for _ in range(n)) for _ in range(m)]
matrix = []
next = []
for i in range(m):
    p = stdin.readline()
    sub = []
    for j in range(len(p)-1):
        if p[j] != " ":
            if p[j] == "-":
                sub.append(p[j]+p[j+1])
            elif j > 0 and p[j-1] == "-":
                continue
            else:
                sub.append(p[j])
            if p[j] == "1":
                next.append([i, len(sub) - 1])
                visited[i][len(sub) - 1] = 1
    matrix.append(sub)

result_cnt = 0
while len(next) > 0:
    next_2 = [next.pop() for _ in range(len(next))]
    while len(next_2) > 0:
        pop = next_2.pop()
        my_bfs(pop[0] + 1, pop[1])
        my_bfs(pop[0], pop[1] + 1)
        my_bfs(pop[0] - 1, pop[1])
        my_bfs(pop[0], pop[1] - 1)
    if len(next) > 0:
        result_cnt += 1
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "0":
            result_cnt = -1
            break
    if result_cnt == -1:
        break
print(result_cnt)
