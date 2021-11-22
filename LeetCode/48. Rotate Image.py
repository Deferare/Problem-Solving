class Solution:
    def rotate(self, nums: List[int]) -> None:
        n = len(nums)
        sub_arr = [list(0 for _ in range(n)) for _ in range(n)]
        index_1 = 0
        for i in range(n):
            index_2 = 0
            for j in range(n).__reversed__():
                sub_arr[index_1][index_2] = nums[j][i]
                index_2 += 1
            index_1 += 1
        del index_1, index_2
        for i in range(n):
            for j in range(n):
                nums[i][j] = sub_arr[i][j]
        del sub_arr
