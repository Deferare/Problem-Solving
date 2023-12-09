class Solution {
    func minPatches(_ nums: [Int], _ n: Int) -> Int {
        var result = 0
        var maxReach = 0, target = 1
        var i = 0
        
        while maxReach < n {
            if i < nums.count && nums[i] <= target {
                maxReach += nums[i]
                i += 1
            } else {
                maxReach += target
                result += 1
            }
            
            target = maxReach + 1
        }
            
        return result
    }
}
