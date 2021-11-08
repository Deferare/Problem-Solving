n = int(input())
seat = input()
d = {"S":0, "L":0}
for i in range(n):
    d[seat[i]] += 1
seat_able = 0
if d["S"] > 0:
    seat_able = d["S"]+1
if d["L"] > 0:
    seat_able += (d["L"]//2)
print(min(seat_able,n))
