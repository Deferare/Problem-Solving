class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for s in magazine:
            if not d.__contains__(s):
                d[s] = 1
            else:
                d[s] += 1
        for s in ransomNote:
            if not d.__contains__(s): return False
            d[s] -= 1;
            if d[s] < 0: return False
        return True
