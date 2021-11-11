from sys import stdin
score = stdin.readline().strip()
if len(score) == 1:
    result = "0.0"
else:
    result = ""
    if score[0] == "A":
        result = "4"
    elif score[0] == "B":
        result = "3"
    elif score[0] == "C":
        result = "2"
    elif score[0] == "D":
        result = "1"
    if score[1] == "+":
        result += ".3"
    elif score[1] == "0":
        result += ".0"
    else:
        result = str(int(result)-1)+".7"
print(result)
