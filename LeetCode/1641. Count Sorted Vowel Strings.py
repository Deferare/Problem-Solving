class Solution:
    def countVowelStrings(self, n: int) -> int:
        dplist = [[1]*5] * (n+1)
        for i in range(0,n):
            dplist[i][4] = 1
        for i in range(1,n+1):
            for j in range(3,-1,-1):
                dplist[i][j] = dplist[i-1][j] + dplist[i][j+1]
        return dplist[n][0]
        
