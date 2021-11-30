from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) < 1:
                    return False
                if s[i] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(s[i])
                elif s[i] == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append(s[i])
                elif s[i] == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        stack.append(s[i])
        if len(stack) > 0:
            return False
        return True
