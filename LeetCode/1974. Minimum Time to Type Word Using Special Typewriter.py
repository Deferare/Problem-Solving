class Solution:
    def minTimeToType(self, word: str) -> int:
        typewriter = [chr(i) for i in range(97, 97+26)]
        ind = 0
        answer = 0
        pointer = 0
        while ind < len(word):
            if word[ind] == typewriter[pointer]:
                answer += 1
                ind += 1
            else:
                if word[ind] > typewriter[pointer]:
                    needRight = ord(word[ind]) - ord(typewriter[pointer])
                    needLeft = pointer + (123 - ord(word[ind]))
                    answer += min(needRight, needLeft)
                    pointer = pointer + needRight
                elif word[ind] < typewriter[pointer]:
                    needRight = (26 - pointer) + (ord(word[ind]) - 97)
                    needLeft = ord(typewriter[pointer]) - ord(word[ind])
                    answer += min(needRight, needLeft)
                    pointer = pointer + needRight - 26
        return answer
