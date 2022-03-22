class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def createSq(value, x, y, state):
            if value > n*n: return
            matrix[x][y] = value
            key = f"{x}|{y}"
            s.add(key)
            if state == 0:
                key = f"{x}|{y + 1}"
                if key in s or y + 1 >= n:
                    createSq(value + 1, x + 1, y, 1)
                else:
                    createSq(value + 1, x, y + 1, 0)
            elif state == 1:
                key = f"{x + 1}|{y}"
                if key in s or x + 1 >= n:
                    createSq(value + 1, x, y - 1, 2)
                else:
                    createSq(value + 1, x + 1, y, 1)
            elif state == 2:
                key = f"{x}|{y - 1}"
                if key in s or y - 1 < 0:
                    createSq(value + 1, x - 1, y, 3)
                else:
                    createSq(value + 1, x, y - 1, 2)
            elif state == 3:
                key = f"{x - 1}|{y}"
                if key in s or x - 1 < 0:
                    createSq(value + 1, x, y + 1, 0)
                else:
                    createSq(value + 1, x - 1, y, 3)
        s = set()
        matrix = [list(0 for _ in range(n)) for _ in range(n)]
        createSq(1, 0, 0, 0)
        return matrix
