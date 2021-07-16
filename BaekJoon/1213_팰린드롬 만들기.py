word = input()

alpa_dict = {}
for crnt in word:
    if crnt in alpa_dict:
        alpa_dict[crnt] += 1
    else:
        alpa_dict[crnt] = 1

word = sorted(set(word))
str_len = 0
result_str = []
even_check = 0
save = []
for crnt in word:
    if alpa_dict[crnt]%2 != 0:
        alpa_dict[crnt] -= 1
        save.append(crnt)
        even_check += 1
    if even_check > 1:
        save = []
        result_str = "I'm Sorry Hansoo"
        break
    while alpa_dict[crnt] != 0:
        if len(result_str) < 2:
            result_str.append(crnt)
        else:
            result_str.insert(int(len(result_str)/2), crnt)
        alpa_dict[crnt] -= 1

if len(save) > 0:
    result_str.insert(int(len(result_str)/2), save[0])

for crnt in result_str:
    print(crnt, end="")
