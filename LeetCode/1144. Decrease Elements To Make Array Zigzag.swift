class Solution {
    func movesToMakeZigzag(_ nums: [Int]) -> Int {
        var even = 0, odd = 0
        
        for i in 0..<nums.count {
            let left = i > 0 ? nums[i-1] : 1000
            let right = i < nums.count-1 ? nums[i+1] : 1000
            let minNeighbor = min(left, right)
            
            if i%2 == 0 {
                if nums[i] >= minNeighbor {
                    even += nums[i] - minNeighbor + 1
                }
            } else if nums[i] >= minNeighbor {
                odd += nums[i] - minNeighbor + 1
            }
        }
        
        return min(even, odd)
    }
}
