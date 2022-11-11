class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        check = set()
        maxNumber = ""
        for _ in range(0, len(number)):
            removeCheck = False
            crntNumber = ""
            for i in range(0, len(number)):
                if (i in check and number[i] == digit) or number[i] != digit or removeCheck:
                    crntNumber += number[i]
                else:
                    check.add(i)
                    removeCheck = True
                    continue
            if removeCheck: maxNumber = max(crntNumber, maxNumber)
            else: break
        return maxNumber
