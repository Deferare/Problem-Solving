class Solution {
    func minDeletion(_ nums: [Int]) -> Int {
        var count = 0
        var i = 0
        
        while i < nums.count-1 {
            if nums[i] == nums[i+1] {
                count += 1
                i += 1
            } else {
                i += 2
            }
        }
        
        if (nums.count - count)%2 != 0 {
            count += 1
        }
        
        return count
    }
}
