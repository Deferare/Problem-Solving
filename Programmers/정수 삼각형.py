def solution(triangle):
    def getMax(i, j) -> int:
        if i >= len(triangle) or j >= len(triangle[i]): return 0
        if i in memo and j in memo[i]:
            return memo[i][j]
        if not i in memo: memo[i] = dict()

        memo[i][j] = max(getMax(i+1, j), getMax(i+1,j+1)) + triangle[i][j]
        return memo[i][j]

    memo = dict()
    return getMax(0, 0)
