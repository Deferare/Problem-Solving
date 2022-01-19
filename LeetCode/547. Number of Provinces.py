class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def travers(ind_1, ind_2):
            for i in range(ind_2, len(isConnected[ind_1])):
                if isConnected[ind_1][i] == 1 and i not in visited:
                    visited.add(i)
                    travers(i, ind_2)
        result = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                result += 1
                visited.add(i)
                for j in range(len(isConnected[i])):
                    if isConnected[i][j] == 1 and j not in visited:
                        visited.add(j)
                        travers(j, i)
        return result
