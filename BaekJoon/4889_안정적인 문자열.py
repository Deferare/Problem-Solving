from sys import stdin

cnt_check = 0

while True:
    check = 0
    cnt_check += 1
    braces_arr = list(map(str,stdin.readline().strip()))
    sub_save = []
    left_stack = []
    for i in range(len(braces_arr)):
        if braces_arr[i] == "{":
            left_stack.append(i)
        elif braces_arr[i] == "-":
            check = 1
            break
        elif len(left_stack) > 0:
            left_stack.pop()
        elif len(left_stack) == 0:
            sub_save.append(i)
    if check == 1:
        break
    left_len = len(left_stack)
    sub_len = len(sub_save)
    answer = ((left_len//2+left_len%2) + (sub_len//2+sub_len%2))
    print(f"{cnt_check}. {answer}")
