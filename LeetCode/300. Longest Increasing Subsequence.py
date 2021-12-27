class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [[nums[-1]]]
        for i in range(len(nums)-1).__reversed__():
            check = 0
            for j in range(len(arr)).__reversed__():
                if nums[i] < arr[j][-1]:
                    if j == len(arr)-1:
                        arr.append([nums[i]])
                    else:
                        arr[j+1].append(nums[i])
                    check = 1
                    break
            if check == 0:
                arr[0].append(nums[i])
        return len(arr)
