a = input()
b = input()
my_dict = dict()
for i in range(len(a)):
    if a[i] not in my_dict:
        my_dict[a[i]] = 1
    else:
        my_dict[a[i]] += 1
sub_result = 0
for i in range(len(b)):
    if b[i] not in my_dict:
        sub_result += 1
    else:
        my_dict[b[i]] -= 1
        if my_dict[b[i]] == 0:
            del my_dict[b[i]]
for value in my_dict.values():
    sub_result += value
print(sub_result)
