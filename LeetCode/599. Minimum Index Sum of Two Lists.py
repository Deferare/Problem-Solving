class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d_1 = dict()
        d_2 = dict()
        for i in range(len(list1)):
            d_1[list1[i]] = i
        for i in range(len(list2)):
            d_2[list2[i]] = i
        arr = []
        for (key,value) in d_1.items():
            if key in d_2:
                arr.append([key, value+d_2[key]])
        arr.sort(key=lambda x:x[1])
        result_arr = [arr[0][0]]
        for i in range(1, len(arr)):
            if arr[i][1] == arr[i-1][1]:
                result_arr.append(arr[i][0])
            else:
                break
        return result_arr
