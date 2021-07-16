word = input()

result_check = 0
for i in range(len(word)):
    index = i
    last_index = len(word)-1
    check = 0
    while index <= last_index:
        if word[index] != word[last_index]:
            check = 1
            break
        index += 1
        last_index -= 1
    if check == 0:
        break
    result_check += 1

print(result_check+len(word))
