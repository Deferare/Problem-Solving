class Solution {
    func minimumDeletions(_ nums: [Int]) -> Int {
        if nums.count == 3 { return 2 }
        if nums.count < 3 { return nums.count }
        
        var minMax = [(index: 0, value: Int.max), (index: 0, value: Int.min)]
        
        for i in 0..<nums.count {
            if nums[i] < minMax[0].value {
                minMax[0].index = i
                minMax[0].value = nums[i]
            }
            if nums[i] > minMax[1].value {
                minMax[1].index = i
                minMax[1].value = nums[i]
            }
        }
        
        minMax.sort { $0.index < $1.index }
        
        var result = 0
        let left = minMax[0].index + 1
        let right = nums.count - minMax[1].index
        
        if left < right {
            result += left
            result += min(minMax[1].index - left + 1, right)
            
        } else {
            result += right
            result += min(left, nums.count - right - left + 1)
        }

        return result
    }
}
