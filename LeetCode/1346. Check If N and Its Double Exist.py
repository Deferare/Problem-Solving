class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s_1 = set()
        s_2 = set()
        s_1.add(arr[0])
        s_2.add(arr[0] * 2)
        for i in range(1, len(arr)):
            crnt = arr[i] * 2
            if crnt in s_1 or arr[i] in s_2:
                return True
            s_1.add(arr[i])
            s_2.add(crnt)
        return False
