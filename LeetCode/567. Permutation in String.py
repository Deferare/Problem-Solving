class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = dict()
        for i in range(len(s1)):
            if s1[i] not in d: d[s1[i]] = 1
            else: d[s1[i]] += 1
        d2 = d.copy()
        check = 0
        left = -1
        ind = 0
        while ind < len(s2):
            if s2[ind] in d2:
                if d2[s2[ind]] > 0:
                    if left == -1: left = ind
                    d2[s2[ind]] -= 1
                    check += 1
                elif left != -1:
                    for i in range(left, ind):
                        check -= 1
                        left += 1
                        d2[s2[i]] += 1
                        if s2[i] == s2[ind]:
                            break
                    continue
            else:
                d2 = d.copy()
                check = 0
                left = -1
            if check == len(s1): return True
            ind += 1
        return False
