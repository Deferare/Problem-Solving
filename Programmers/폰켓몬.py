def solution(nums):
    dict = {}
    avai = int(len(nums)/2)
    for crnt in nums:
        key = str(crnt)
        if key not in dict:
            dict[key] = 1
    if len(dict) <= avai:
        return len(dict)
    return avai
