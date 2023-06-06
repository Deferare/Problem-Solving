class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        n = len(arr)
        while n > 0:
            max_val = max(arr[:n])
            max_inx = arr.index(max_val)
            if max_val != arr[n-1]:
                arr[:max_inx+1] = arr[:max_inx+1].__reversed__()
                answer.append(max_inx+1)
                arr[:n] = arr[:n].__reversed__()
                answer.append(n)
            n -= 1
        return answer
