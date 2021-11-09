from collections import deque
n = input()
cards = deque()
for i in range(1, int(n)+1):
    cards.append(i)
while len(cards) > 1:
    cards.popleft()
    if len(cards) > 1:
        cards.append(cards.popleft())
print(cards[0])
