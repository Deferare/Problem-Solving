class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def recursion(crnt, start):
            if start >= N:
                result.append(crnt)
                return
            new_crnt = crnt.copy()
            for i in range(start, N):
                new_crnt.append(s[i])
                if pCheck(start, i):
                    if i != start:
                        new_p = s[start:i + 1]
                        crnt.append(new_p)
                        recursion(crnt.copy(), i + 1)
                        crnt.pop()
                    else: recursion(new_crnt.copy(), i + 1)

        def pCheck(ind_1, ind_2):
            while ind_1 < ind_2:
                if s[ind_1] != s[ind_2]: return False
                ind_1 += 1
                ind_2 -= 1
            return True

        N = len(s)
        result = []
        recursion([], 0)
        return result
