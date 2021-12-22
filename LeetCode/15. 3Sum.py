class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        index_1 = 0
        s = set()
        while index_1 < len(nums)-2:
            index_2 = index_1 + 1
            index_3 = len(nums)-1
            while index_2 < index_3:
                two_sum = nums[index_2] + nums[index_3]
                if two_sum + nums[index_1] > 0:
                    index_3 -= 1
                elif two_sum + nums[index_1] < 0:
                    index_2 += 1
                else:
                    if two_sum + nums[index_1] == 0:
                        key = f"{nums[index_1]}|{nums[index_2]}|{nums[index_3]}"
                        if key not in s:
                            result.append([nums[index_1], nums[index_2], nums[index_3]])
                            s.add(key)
                        index_2 += 1
            index_1 += 1
            if nums[index_1] > 0:
                return result
        return result
