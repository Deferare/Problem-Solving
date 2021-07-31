from sys import stdin

cnt_check = 0

while True:
    check = 0
    cnt_check += 1
    braces_arr = list(map(str,stdin.readline().strip()))
    sub_save = 0
    left_save = 0
    for i in range(len(braces_arr)):
        if braces_arr[i] == "{":
            left_save += 1
        elif braces_arr[i] == "-":
            check = 1
            break
        elif left_save > 0:
            left_save -= 1
        elif left_save == 0:
            sub_save += 1
    if check == 1:
        break
    answer = ((left_save//2+left_save%2) + (sub_save//2+sub_save%2))
    print(f"{cnt_check}. {answer}")
