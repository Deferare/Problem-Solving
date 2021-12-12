class Solution:
    def fib(self, n: int) -> int:
        memo = dict()
        def recursion(index):
            if index <= 0:
                return 0
            if index == 1:
                return 1
            if index in memo:
                return memo[index]
            memo[index] = recursion(index-1) + recursion(index-2)
            return memo[index]
        return recursion(n)
