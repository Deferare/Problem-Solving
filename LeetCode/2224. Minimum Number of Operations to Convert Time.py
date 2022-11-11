import datetime
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        a = datetime.timedelta(hours=int(current[0] + current[1]), minutes=int(current[3] + current[4])).seconds
        b = datetime.timedelta(hours=int(correct[0] + correct[1]), minutes=int(correct[3] + correct[4])).seconds
        diffSecond = int(b-a)
        answer = 0
        while diffSecond > 0:
            if (diffSecond-3600) >= 0: diffSecond -= 3600
            elif (diffSecond-900) >= 0: diffSecond -= 900
            elif (diffSecond - 300) >= 0: diffSecond -= 300
            elif (diffSecond - 60) >= 0: diffSecond -= 60
            answer += 1
        return answer
        
