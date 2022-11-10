class Solution:
    def maximumTime(self, time: str) -> str:
        arr = [time[0], time[1], ":",time[3], time[4]]
        if arr[0] == "?":
            if arr[1] <= "3" or arr[1] == "?":
                arr[0] = "2"
            else: arr[0] = "1"
        if arr[1] == "?":
            if arr[0] == "1" or arr[0] == "0": arr[1] = "9"
            else: arr[1] = "3"
        if arr[3] == "?": arr[3] = "5"
        if arr[4] == "?": arr[4] = "9"
        answer = ""
        for v in arr: answer += v
        return answer
