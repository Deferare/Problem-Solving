class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        N = len(nums1)
        d = dict()
        for i in range(N):
            for j in range(N):
                crnt = nums1[i] + nums2[j]
                if crnt not in d: d[crnt] = 1
                else: d[crnt] += 1
        result = 0
        for i in range(N):
            for j in range(N):
                crnt = -(nums3[i] + nums4[j])
                if crnt in d:
                    result += d[crnt]
        return result
