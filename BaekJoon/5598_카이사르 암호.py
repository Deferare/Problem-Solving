A = input()
result = ""
for i in range(len(A)):
    convert_a = ord(A[i])-3
    if convert_a < 65:
        convert_a = 91-(65-convert_a)
    result += chr(convert_a)
print(result)
