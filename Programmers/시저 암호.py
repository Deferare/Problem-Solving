def solution(s, n):
    result = ""
    for i in range(len(s)):
        if s[i] == " ":
            result += " "
        else:
            asci_value = ord(s[i])
            if asci_value >= 65 and asci_value <= 90:
                if asci_value+n > 90:
                    asci_value = ((asci_value+n)-90)+64
                else:
                    asci_value += n
            else:
                if asci_value+n > 122:
                    asci_value = ((asci_value+n)-122)+96
                else:
                    asci_value += n
            result += chr(asci_value)
    return result
