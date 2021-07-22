n = int(input())
sum_number = 0
plus_number = 1
while sum_number <= n-plus_number:
    sum_number += plus_number
    plus_number += 1
print(plus_number-1)
