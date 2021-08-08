class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2 = list(set(nums2))
        result_arr = []
        for crnt in nums2:
            if crnt in nums1_set:
                result_arr.append(crnt)
        return result_arr
