s = input()
left_check = 0
right_check = 0
status = s[0]
for i in range(1, len(s)):
    if s[i] != status:
        if s[i] == "1":
            left_check += 1
        else:
            right_check += 1
        status = s[i]
print(max(left_check,right_check))
