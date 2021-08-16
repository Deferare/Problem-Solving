class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        check_dict = {}
        for word in words:
            if word in check_dict:
                check_dict[word] += 1
            else:
                check_dict[word] = 1
        check_arr = list(zip(check_dict.keys(), check_dict.values()))
        check_arr = sorted(check_arr, key=lambda x:x[0], reverse=False)
        check_arr = sorted(check_arr, key=lambda x:x[1], reverse=True)
        result_arr = []
        for i in range(k):
            result_arr.append(check_arr[i][0])
        return result_arr
