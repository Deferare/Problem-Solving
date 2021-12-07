from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = deque()
        for i in range(len(tokens)):
            if tokens[i] == "+":
                arr.append(arr.pop()+arr.pop())
            elif tokens[i] == "-":
                a = arr.pop()
                b = arr.pop()
                arr.append(b-a)
            elif tokens[i] == "*":
                arr.append(arr.pop() * arr.pop())
            elif tokens[i] == "/":
                a = arr.pop()
                b = arr.pop()
                arr.append(int(b/a))
            else:
                arr.append(int(tokens[i]))
        return arr[0]
