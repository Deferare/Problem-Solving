class Solution:
    def average(self, salary: List[int]) -> float:
        salary_len = len(salary)
        min_n = salary[0]
        max_n = 0
        sum_n = 0
        for i in range(salary_len):
            if salary[i] < min_n: min_n = salary[i]
            if salary[i] > max_n: max_n = salary[i]
            sum_n += salary[i]
        sum_n -= max_n
        sum_n -= min_n
        result = sum_n/(salary_len-2)
        return result
