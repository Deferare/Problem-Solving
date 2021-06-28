class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = list(nums)
        def qSort(indexo_1, indexo_2):
            len_check = len(arr)
            if indexo_1 < 0 or indexo_2 < 0 or indexo_1 >= len_check or indexo_2 >= len_check:
                return
            if indexo_2 - indexo_1 <= 1:
                if arr[indexo_1] > arr[indexo_2]:
                    tmp = arr[indexo_1]
                    arr[indexo_1] = arr[indexo_2]
                    arr[indexo_2] = tmp
                return
            index_1 = indexo_1;
            index_2 = indexo_2
            pibot_index = indexo_1 + int((indexo_2 - indexo_1) / 2)
            pibot = arr[pibot_index]
            arr[pibot_index] = arr[indexo_2]
            arr[indexo_2] = pibot
            index_2 -= 1
            while True:
                if arr[index_1] >= pibot and arr[index_2] <= pibot:
                    tmp = arr[index_1]
                    arr[index_1] = arr[index_2]
                    arr[index_2] = tmp
                    index_1 += 1;
                    index_2 -= 1
                elif arr[index_1] <= pibot and arr[index_2] >= pibot:
                    index_1 += 1;
                    index_2 -= 1
                elif arr[index_1] <= pibot:
                    index_1 += 1
                elif arr[index_2] >= pibot:
                    index_2 -= 1
                if index_1 > index_2:
                    break
            arr[indexo_2] = arr[index_1]
            arr[index_1] = pibot
            qSort(indexo_1, index_1)
            qSort(index_1, indexo_2)
        qSort(0, len(arr) - 1)
        return arr
