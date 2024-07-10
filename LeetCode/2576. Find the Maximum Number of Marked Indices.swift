class Solution {
    func maxNumOfMarkedIndices(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var count = 0
        let n = nums.count
        var i = 0
        var j = n / 2
        
        while i < n / 2 && j < n {
            if sorted[i] * 2 <= sorted[j] {
                count += 2
                i += 1
            }
            
            j += 1
        }
        
        return count
    }
}
