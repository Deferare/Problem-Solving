class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = [[] for _ in range(10)]
        bias = 97
        for i in range(2, 10):
            bias2 = 0
            if i == 7 or i == 9: bias2 = 1
            for _ in range(3 + bias2):
                keypad[i].append(chr(bias))
                bias += 1
        arr = []
        for i in range(len(digits)):
            arr.append(keypad[int(digits[i])])
        def recursion(index_1):
            if index_1 >= len(arr):
                return
            for i in range(len(arr[index_1])):
                crnt.append(arr[index_1][i])
                recursion(index_1 + 1)
                if len(crnt) == len(arr):
                    crnt_str = ""
                    for j in range(len(crnt)):
                        crnt_str += crnt[j]
                    result.append(crnt_str)
                crnt.pop()
        result = []
        crnt = []
        recursion(0)
        return result
