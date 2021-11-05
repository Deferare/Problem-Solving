from collections import deque
def solution(number, k):
    le = len(number)
    number = deque(number)
    stack = [number.popleft()]
    cnt = 0
    while cnt < k and len(number) > 0:
        pop = number.popleft()
        if stack[-1] >= pop:
            stack.append(pop)
        else:
            while len(stack) > 0:
                if stack[-1] >= pop:
                    break
                stack.pop()
                cnt += 1
                if cnt == k:
                    break
            stack.append(pop)
        if cnt == k:
            break
    result = ""
    for i in range(len(stack)):
        if len(result) >= le-k:
            break
        result += stack[i]
    for i in range(len(number)):
        if len(result) >= le-k:
            break
        result += number[i]
    return result
