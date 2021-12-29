class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        while n:
            n //= 5
            answer += n
        return answer
