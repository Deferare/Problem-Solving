class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = dict()
        for i in range(len(p)):
            if p[i] not in d: d[p[i]] = 1
            else: d[p[i]] += 1
        result = []
        start = 0
        i = start
        while i < len(s):
            if s[i] not in d:
                if s[start] not in d: d[s[start]] = 1
                else: d[s[start]] += 1
                start += 1
                continue
            else:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                    if len(d) == 0:
                        result.append(start)
            i += 1
        return result
