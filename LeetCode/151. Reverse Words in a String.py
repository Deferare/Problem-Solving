class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.split(" "))
        arr.reverse()
        result = ""
        for i in range(len(arr)-1):
            if arr[i] != "":
                result += arr[i]
                result += " "
        if arr[-1] != "":
            result += arr[-1]
        else:
            result = result[:len(result)-1]
        return result
