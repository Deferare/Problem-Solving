class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for _ in range(numRows-1):
            next_pas = [1]
            for i in range(1, len(pascal[-1])):
                next_pas.append(pascal[-1][i-1]+pascal[-1][i])
            next_pas.append(1)
            pascal.append(next_pas)
        return pascal
