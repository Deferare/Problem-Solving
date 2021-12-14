class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def mySearch(index_1, index_2):
            if index_1 >= n or index_2 >= m:
                return False
            value = matrix[index_1][index_2]
            if value == 1000000000:
                return False
            matrix[index_1][index_2] = 1000000000
            if value == target:
                return True
            elif value > target:
                return False
            if mySearch(index_1 + 1, index_2) or mySearch(index_1, index_2 + 1):
                return True
            return False

        n = len(matrix)
        m = len(matrix[0])
        return mySearch(0, 0)
