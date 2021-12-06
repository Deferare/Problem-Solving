from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        check = 0
        deadends = set(deadends)
        q = deque([["0000"]])
        while len(q) > 0:
            pop = q.popleft()
            q_next = []
            for i in range(len(pop)):
                if pop[i] not in deadends:
                    if pop[i] == target:
                        return check
                    deadends.add(pop[i])
                    for j in range(4):
                        crnt_str_1 = pop[i][:j]
                        crnt_str_2 = pop[i][:j]
                        n_crnt = int(pop[i][j])
                        if n_crnt + 1 > 9:
                            n_crnt = -1
                        crnt_str_1 += str(n_crnt + 1)
                        crnt_str_1 += pop[i][j + 1:]
                        n_crnt = int(pop[i][j])
                        if n_crnt - 1 < 0:
                            n_crnt = 10
                        crnt_str_2 += str(n_crnt - 1)
                        crnt_str_2 += pop[i][j + 1:]
                        if crnt_str_1 not in deadends:
                            q_next.append(crnt_str_1)
                        if crnt_str_2 not in deadends:
                            q_next.append(crnt_str_2)
            check += 1
            if len(q_next) > 0:
                q.append(q_next.copy())
                q_next.clear()
        return -1
