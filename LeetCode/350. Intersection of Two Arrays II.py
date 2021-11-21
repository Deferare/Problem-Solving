class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = dict()
        for i in range(len(nums1)):
            if nums1[i] not in nums1_dict:
                nums1_dict[nums1[i]] = 1
            else:
                nums1_dict[nums1[i]] += 1
        nums2_dict = dict()
        for i in range(len(nums2)):
            if nums2[i] in nums1_dict:
                if nums2[i] not in nums2_dict:
                    nums2_dict[nums2[i]] = 1
                else:
                    nums2_dict[nums2[i]] += 1
        result = []
        for (key, value) in nums2_dict.items():
            iter_n = min(nums1_dict[key], nums2_dict[key])
            for _ in range(iter_n):
                result.append(key)
        return result
