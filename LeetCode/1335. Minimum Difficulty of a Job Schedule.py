class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        # 일감이 일수보다 작으면,
        N = len(jobDifficulty)
        if N < d:
            return -1

        # job은 jobDifficulty에서 선택 하기 위한 인덱스 정수,
        # day에는 며칠이 흘렀는가에 대한 정수.
        def dp(job, day):

            # 목표 일이면, 현재에서 취할 수 있는 가장 큰 값을 리턴.
            if day == d:
                return jobs_max[job]
            if cache[job][day] != 10000000: return cache[job][day]

            # 당장 취할 수 있는 일감부터,
            # 원하는 일수를 채우기 위해서 남겨두어야 하는 갯수 까지를 하나하나 대입해 보면서,
            # 재귀 적으로 다음 day를 호출함.
            crnt = 0
            for i in range(job, N - (d - day)):
                crnt = max(crnt, jobDifficulty[i])
                cache[job][day] = min(cache[job][day], crnt + dp(i + 1, day + 1))
            return cache[job][day]

        # jobDifficultry에서 오른쪽부터 탐색하여 현재까지의 max 값을 채우는
        # 새로운 배열을 jobs_max에 할당함.
        jobs_max = list(0 for _ in range(N))
        crnt = 0
        for i in range(1, N + 1):
            crnt = max(crnt, jobDifficulty[-i])
            jobs_max[-i] = crnt
        cache = [list(10000000 for _ in range(d)) for _ in range(N)]
        return dp(0, 1)
