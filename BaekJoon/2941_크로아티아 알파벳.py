word = input()
word_len = len(word)
cnt = 0
index = 0
while index < word_len:
    if index+2 <= word_len:
        sub_word_1 = word[index:index+2]
        if sub_word_1 == "c=" or sub_word_1 == "c-":
            index += 1
        elif sub_word_1 == "lj":
            index += 1
        elif sub_word_1 == "nj":
            index += 1
        elif sub_word_1 == "s=":
            index += 1
        elif sub_word_1 == "z=":
            index += 1
        elif sub_word_1 == "d-":
            index += 1
        elif index+3 <= word_len:
            if word[index:index+3] == "dz=":
                index += 2
    index += 1
    cnt += 1
print(cnt)
