class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        save = []
        index = 0
        while len(save) < len(arr):
            save.append(arr[index])
            if arr[index] == 0:
                save.append(arr[index])
            index += 1
        for i in range(len(arr)):
            arr[i] = save[i]
