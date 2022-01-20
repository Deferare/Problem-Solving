n = int(input())
cards = list(map(int, input().split(" ")))
for i in range(1, len(cards)):
    start = 0
    end = i - 1
    max_check = cards[i]
    while start <= end:
        crnt = cards[start] + cards[end]
        if crnt > max_check:
            max_check = crnt
        start += 1
        end -= 1
    cards[i] = max_check
print(cards[-1])
