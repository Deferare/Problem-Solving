class Solution:
    def splitNum(self, num: int) -> int:
        num_arr = sorted(str(num))
        return int("".join(num_arr[::2])) + int("".join(num_arr[1::2]))
