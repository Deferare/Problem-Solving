class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1_len = len(num1)
        num2_len = len(num2)

        arr = []
        over_num = "0"
        for i in range(1, max(num1_len, num2_len)+1):
            if i > num1_len:
                n_1 = int(over_num)
                over_num = "0"
            else:
                n_1 = int(num1[-i])
            if i > num2_len:
                n_2 = int(over_num)
                over_num = "0"
            else:
                n_2 = int(num2[-i])
            new_n = str(n_1 + n_2 + int(over_num))
            if len(new_n) > 1:
                arr.append(str(new_n)[1])
                over_num = str(new_n)[:-1]
            else:
                arr.append(new_n)
                over_num = "0"
        answer = over_num
        for i in range(1, len(arr) + 1): answer += arr[-i]
        return str(int(answer))
