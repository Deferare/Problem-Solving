from sys import stdin

n = int(stdin.readline())
result_check = 0
for _ in range(n):
    word = stdin.readline().strip()
    stack = [word[0]]
    for i in range(1, len(word)):
        if len(stack) != 0:
            if word[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(word[i])
        else:
            stack.append(word[i])
    if len(stack) == 0:
        result_check += 1
        
print(result_check)
