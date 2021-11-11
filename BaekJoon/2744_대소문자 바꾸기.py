S = input()
result = ""
for i in range(len(S)):
    convert_s = ord(S[i])
    if convert_s < 97:
        result += chr(convert_s+32)
    else:
        result += chr(convert_s-32)
print(result)
