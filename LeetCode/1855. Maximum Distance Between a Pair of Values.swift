class Solution {
    func maxDistance(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var maxDist = 0
        
        for i in 0..<nums1.count {
            var j = i + maxDist
            
            while j < nums2.count {
                if nums1[i] <= nums2[j] { j += 1 }
                else { break }
            }
            
            maxDist = max(maxDist, j-i)
        }
        
        return max(0, maxDist-1)
    }
}
