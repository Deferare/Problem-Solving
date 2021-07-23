class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_index_memo = {}
        for i in range(len(s)):
            end_index_memo[s[i]] = i
        result_arr = []
        index = 0
        while index < len(s):
            starting_point = index
            target_point = end_index_memo[s[index]]
            while index < target_point:
                if end_index_memo[s[index]] > target_point:
                    target_point = end_index_memo[s[index]]
                index += 1
            index += 1
            result_arr.append(index-starting_point)
        return result_arr
