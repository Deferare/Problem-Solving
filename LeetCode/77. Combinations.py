class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(num):
            if len(crnt_arr) == k:
                arr.append(crnt_arr.copy())
            for i in range(num, n + 1):
                if len(crnt_arr) == 0 or i > crnt_arr[-1]:
                    crnt_arr.append(i)
                    visited.add(i)
                    recursion(num + 1)
                    crnt_arr.pop()
                    visited.remove(i)

        arr = []
        crnt_arr = []
        visited = set()
        recursion(1)
        return arr
