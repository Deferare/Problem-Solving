from collections import deque

def solution(s):
    result_cnt = 0
    q = deque(crnt for crnt in s)
    pre_q = q.copy()
    for _ in range(len(s)):
        bracket = []
        i = 0
        while i < len(s):
            pop = q.popleft()
            if len(bracket) > 0:
                if bracket[-1] == "[" and pop == "]":
                    bracket.pop()
                elif bracket[-1] == "(" and pop == ")":
                    bracket.pop()
                elif bracket[-1] == "{" and pop == "}":
                    bracket.pop()
                else:
                    bracket.append(pop)
            else:
                bracket.append(pop)
            i += 1
        if len(bracket) == 0:
            result_cnt += 1
        pre_q.append(pre_q.popleft())
        q = pre_q.copy()
    return result_cnt
