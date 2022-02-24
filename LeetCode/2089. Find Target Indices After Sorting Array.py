class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        left = 0; right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                while mid >= 0:
                    if nums[mid] == target:
                        mid -= 1
                    else:
                        mid += 1
                        break
                if mid < 0: mid += 1
                while mid < len(nums):
                    if nums[mid] == target:
                        result.append(mid)
                        mid += 1
                    else: break
                break
        return result
