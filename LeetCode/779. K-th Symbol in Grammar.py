class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def myRecursion(N, K):
            if N == 1:
                return 0
            if K % 2 == 1:
                return myRecursion(N - 1, (K + 1) // 2)
            else:
                if myRecursion(N - 1, K // 2) == 0:
                    return 1
                else:
                    return 0
        return myRecursion(n, k)
