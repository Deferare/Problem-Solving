from sys import stdin

while True:
    word = stdin.readline().strip()
    if word == "*":
        break
    check = 0
    for i in range(1, len(word)-1):
        save_set = set()
        for j in range(len(word)-i):
            sub_word = word[j]+word[j+i]
            if sub_word not in save_set:
                save_set.update([sub_word])
            else:
                check = 1
                break
        if check == 1:
            break
    if check == 0:
        print(f"{word} is surprising.")
    else:
        print(f"{word} is NOT surprising.")
