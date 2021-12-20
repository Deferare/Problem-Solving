class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        turn = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if turn == 0 and arr[i] < arr[i - 1]:
                turn = 1
            if turn == 1 and arr[i] > arr[i - 1]:
                return False
        if turn == 0:
            return False
        return True
