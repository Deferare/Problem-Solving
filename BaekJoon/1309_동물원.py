n = int(input())
first = [1,1]
second = [3,2]
index = 1
while index != n:
    second = [first[0] + first[1] + first[1], first[0] + first[1]]
    first = second
    index += 1
print((sum(first)+first[1])%9901)
