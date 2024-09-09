class Solution {
    func smallestRangeII(_ nums: [Int], _ k: Int) -> Int {
        let sortedNums = nums.sorted()
        let n = nums.count
        var result = sortedNums[n - 1] - sortedNums[0]
        
        for i in 0..<n - 1 {
            let minValue = min(sortedNums[0] + k, sortedNums[i + 1] - k)
            let maxValue = max(sortedNums[n - 1] - k, sortedNums[i] + k)
            
            result = min(result, maxValue - minValue)
        }
        
        return result
    }
}
