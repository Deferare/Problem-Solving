class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        len_str = len(s)
        result_n = 0
        index = 0
        while index < len_str:
            if s[index] == "I":
                if index+1 < len_str and (s[index+1] == "V" or s[index+1] == "X"):
                    result_n += romans[s[index + 1]] - romans[s[index]]
                    index += 1
                else:
                    result_n += romans[s[index]]
            elif s[index] == "X":
                if index+1 < len_str and (s[index+1] == "L" or s[index+1] == "C"):
                    result_n += romans[s[index + 1]] - romans[s[index]]
                    index += 1
                else:
                    result_n += romans[s[index]]
            elif s[index] == "C":
                if index+1 < len_str and (s[index+1] == "D" or s[index+1] == "M"):
                    result_n += romans[s[index + 1]] - romans[s[index]]
                    index += 1
                else:
                    result_n += romans[s[index]]
            else:
                result_n += romans[s[index]]
            index += 1
        return result_n
