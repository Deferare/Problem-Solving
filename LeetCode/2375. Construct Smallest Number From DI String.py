class Solution:
    def smallestNumber(self, pattern: str) -> str:
        length = len(pattern)
        crntChar = []
        for i in range(0, length+1):
            if i >= length: crntChar.append(crntChar[-1])
            else: crntChar.append(pattern[i])
        answer = []
        lastI = 0
        for i in range(0, length+1):
            answer.insert(lastI, i+1)
            if crntChar[i] == "I":
                lastI = i+1
        answer2 = ""
        for c in answer:
            answer2 += c.__str__()
        return answer2
