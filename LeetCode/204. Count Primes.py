class Solution:
    def countPrimes(self, n: int) -> int:
        my_numbers = [True for _ in range(n+2)]
        my_numbers[0], my_numbers[1] = False, False
        for i in range(2, int(n**0.5)+1):
            if my_numbers[i]:
                j = i*2
                while j < n:
                    my_numbers[j] = False
                    j += i
        cnt_result = 0
        for i in range(1, len(my_numbers)-2):
            if my_numbers[i]:
                cnt_result += 1
        return cnt_result
