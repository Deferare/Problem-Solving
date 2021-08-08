class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        key = []
        rank_dict = {}
        for i in range(len(mat)):
            sub_cnt = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    sub_cnt += 1
            if sub_cnt not in rank_dict:
                rank_dict[sub_cnt] = [i]
            else:
                rank_dict[sub_cnt].append(i)
            key.append(sub_cnt)
        key = list(set(key))
        key.sort()
        result_arr = []
        while len(result_arr) < k:
            pop = key.pop(0)
            rank_dict[pop].sort()
            for crnt in rank_dict[pop]:
                result_arr.append(crnt)
                if len(result_arr) == k:
                    break
        return result_arr
