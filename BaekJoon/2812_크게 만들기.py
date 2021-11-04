from sys import stdin

n,m = map(int, stdin.readline().split(" "))
arr = [int(crnt) for crnt in stdin.readline().strip()]
stack = []
cnt = 0
for i in range(n):
    if len(stack) == 0:
        stack.append(i)
    else:
        if arr[i] <= arr[stack[-1]]:
            stack.append(i)
        else:
            while len(stack) > 0:
                if arr[stack[-1]] < arr[i]:
                    arr[stack.pop()] = -1
                    cnt += 1
                else:
                    break
                if cnt == m:
                    break
            stack.append(i)
    if cnt == m:
        break
cnt = 0
for i in range(n):
    if cnt == n - m:
        break
    if arr[i] != -1:
        print(str(arr[i]), end="")
        cnt += 1
