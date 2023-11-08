class Solution {
    func minimizeMax(_ nums: [Int], _ p: Int) -> Int {
        let sortedNums = nums.sorted()
        var left = 0
        var right = sortedNums.last! - sortedNums.first!
        
        while left < right {
            let mid = left + (right - left)/2
            var crntFormed = 0
            var i = 0
            
            while i < sortedNums.count-1, crntFormed < p {
                if sortedNums[i+1] - sortedNums[i] <= mid {
                    i += 2
                    crntFormed += 1
                } else { i += 1 }
            }
            
            if crntFormed >= p { right = mid } 
            else { left = mid + 1 }
        }
        
        return left
    }
}
