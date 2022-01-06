class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums = len(nums1) + len(nums2)
        crnt_num = 0
        crnt_num_2 = 0
        if len(nums1) > 0:
            crnt_num = nums1[0]
        if len(nums2) > 0:
            crnt_num_2 = nums2[0]
        len_crnt = len_nums//2
        index_a = 0
        index_b = 0
        while index_a + index_b <= len_crnt:
            if len(nums1) > 0 and (index_b >= len(nums2) or (index_a < len(nums1) and nums1[index_a] < nums2[index_b])):
                crnt_num_2 = crnt_num
                crnt_num = nums1[index_a]
                index_a += 1
            elif len(nums2) > 0:
                crnt_num_2 = crnt_num
                crnt_num = nums2[index_b]
                index_b += 1
            else:
                break
        if len_nums%2 == 0:
            return (crnt_num+crnt_num_2)/2
        return crnt_num
