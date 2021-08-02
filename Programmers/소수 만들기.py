def solution(nums):
    nums_len = len(nums)
    answer = 0
    index_1 = 0
    while index_1 <= nums_len-3:
        for i in range(index_1+1, nums_len-1):
            for j in range(i+1, nums_len):
                sub_sum = nums[index_1] + nums[i] + nums[j]
                check = 0
                for k in range(2, int(sub_sum/2)):
                    if sub_sum%k == 0:
                        check = 1
                        break
                if check == 0:
                    answer += 1
        index_1 += 1
    return answer
