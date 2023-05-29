class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        first_none_nine = 0
        for i in range(len(num_str)):
            if num_str[i] != "9":
                first_none_nine = i
                break
        max_num = num_str.replace(num_str[first_none_nine], "9")
        min_num = num_str.replace(num_str[0], "0")
        return int(max_num) - int(min_num)
