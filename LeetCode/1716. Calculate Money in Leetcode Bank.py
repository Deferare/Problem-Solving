class Solution:
    def totalMoney(self,n: int) -> int:
        result = 0
        mondaySave = 1
        n = n
        while True:
            if n <= 7:
                save = mondaySave
                for i in range(0,n):
                    result += save
                    save += 1
                break
            quotient = n // 7
            mondaySave += quotient
            n = n%7
            result += quotient * 28
            if quotient > 1:
                plus = 7
                for i in range(2, quotient):
                    plus += i * 7
                result += plus
        return result
        
