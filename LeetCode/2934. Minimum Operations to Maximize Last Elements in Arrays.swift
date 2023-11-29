class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        if n == 1 { return 0 }
        
        var result = 0
        
        for i in stride(from: n-2, to: -1, by: -1) {
            if nums1[i] <= nums1[n-1] && nums2[i] <= nums2[n-1] { continue }
            if nums1[i] <= nums2[n-1] && nums2[i] <= nums1[n-1] { result += 1 }
            else { return -1 }
        }
        
        var nums1 = nums1
        var nums2 = nums2
        let tmp = nums1[n-1]
        nums1[n-1] = nums2[n-1]
        nums2[n-1] = tmp
        
        var result2 = 1
        
        for i in stride(from: n-2, to: -1, by: -1) {
            if nums1[i] <= nums1[n-1] && nums2[i] <= nums2[n-1] { continue }
            if nums1[i] <= nums2[n-1] && nums2[i] <= nums1[n-1] { result2 += 1 }
        }
        
        return min(result, result2)
    }
}
