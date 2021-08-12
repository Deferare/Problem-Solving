class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        save_arr = ["" for _ in range(len(s))]
        for i in range(len(s)):
            save_arr[indices[i]] = s[i]
        result = ""
        for crnt in save_arr:
            result += crnt
        return result
