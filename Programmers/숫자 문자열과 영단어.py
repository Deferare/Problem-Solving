def solution(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i] == "z":
            result += "0"
            i += 4
        elif s[i] == "o":
            result += "1"
            i += 3
        elif s[i] == "t":
            if s[i+1] == "w":
                result += "2"
                i += 3
            elif s[i+1] == "h":
                result += "3"
                i += 5
        elif s[i] == "f":
            if s[i+1] == "o":
                result += "4"
            elif s[i+1] == "i":
                result += "5"
            i += 4
        elif s[i] == "s":
            if s[i+1] == "i":
                result += "6"
                i += 3
            elif s[i+1] == "e":
                result += "7"
                i += 5
        elif s[i] == "e":
            result += "8"
            i += 5
        elif s[i] == "n":
            result += "9"
            i += 4
        else:
            result += s[i]
            i += 1
    return int(result)
