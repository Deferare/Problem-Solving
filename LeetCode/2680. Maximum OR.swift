class Solution {
    func maximumOr(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefixOr = Array(repeating: 0, count: n)
        var suffixOr = Array(repeating: 0, count: n)
        
        var prefix = 0
        var suffix = 0
        
        for i in 0..<n {
            prefix = prefix | nums[i]
            prefixOr[i] = prefix
            suffix = suffix | nums[n - 1 - i]
            suffixOr[n - 1 - i] = suffix
        }

        var maxOrValue = 0
        
        for i in 0..<n {
            let modified = nums[i] << k
            let leftOr = i > 0 ? prefixOr[i - 1] : 0
            let rightOr = i < n - 1 ? suffixOr[i + 1] : 0
            
            maxOrValue = max(maxOrValue, modified | leftOr | rightOr)
        }
        
        return maxOrValue
    }
}
