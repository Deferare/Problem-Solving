class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sumDivisibleBy(k):
            p = n // k
            return k * (p * (p + 1)) // 2
        
        return sumDivisibleBy(3) + sumDivisibleBy(5) + sumDivisibleBy(7) - sumDivisibleBy(15) - sumDivisibleBy(21) - sumDivisibleBy(35) + sumDivisibleBy(105)
