class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def myDfs(arr):
            while len(arr) > 0:
                num = arr.pop()
                if num not in d:
                    visited.add(num)
                else:
                    cache.add(num)
                    arr_next = []
                    for i in range(len(d[num])):
                        if d[num][i] in cache: return False
                        arr_next.append(d[num][i])
                    del d[num]
                    if not myDfs(arr_next): return False
                    cache.remove(num)

            return True
        d = dict()
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in d:
                d[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                d[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set()
        arr = [i for i in range(numCourses).__reversed__()]
        cache = set()
        return myDfs(arr)
