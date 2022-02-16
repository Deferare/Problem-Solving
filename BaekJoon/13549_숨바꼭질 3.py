from collections import deque

N, K = map(int, input().split(" "))
dp = dict()
dp[N] = 0
q = deque([[N-1, 0], [N+1, 0], [N*2, -1]])

while len(q) > 0:
    q_next = deque()
    while len(q) > 0:
        pop = q.popleft()
        if pop[0] < 0 or pop[0] > K + N: continue
        if pop[0] not in dp or dp[pop[0]] > pop[1] + 1:
            dp[pop[0]] = pop[1] + 1
            q_next.append([pop[0] - 1, pop[1] + 1])
            q_next.append([pop[0] + 1, pop[1] + 1])
            q_next.append([pop[0] * 2, pop[1]])
    q = q_next
    
print(dp[K])
