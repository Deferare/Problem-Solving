class Solution:
    def myAtoi(self, s: str) -> int:
        n = ""
        index = 0
        turn = 0
        while index < len(s):
            if s[index] != " ":
                asci = ord(s[index])
                if asci == 43 or asci == 45:
                    if turn == 1:
                        break
                    n += chr(asci)
                    turn = 1
                elif asci >= 48 and asci <= 57:
                    n += chr(asci)
                    turn = 1
                else:
                    break
            elif turn != 0:
                break
            index += 1
        try:
            n = int(n)
            if n >= 2**31:
                n = 2**31-1
            elif n <= -(2**31):
                n = -(2**31)
        except:
            return 0
        return n
