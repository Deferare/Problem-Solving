import math


def solution(numbers):
    visited = set()
    goal = set()
    def prime_checker(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    def recursion(index, crnt):
        if index in visited:
            n = ""
            for i in range(len(crnt)):
                n += crnt[i]
            n = int(n)
            if n > 1:
                if prime_checker(n):
                    goal.add(n)
            if len(visited) != len(numbers):
                return
        if len(visited) == len(numbers):
            return
        for i in range(len(numbers)):
            if i not in visited:
                crnt.append(numbers[index])
                visited.add(index)
                recursion(i, crnt)
                visited.remove(index)
                crnt.pop()
    for i in range(len(numbers)):
        recursion(i, [])
    return len(goal)
