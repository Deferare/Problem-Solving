class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var maxFreq = 0, left = 0, total = 0
        
        for right in 0..<sorted.count {
            total += sorted[right]
            while (sorted[right] * (right - left + 1)) - total > k {
                total -= sorted[left]
                left += 1
            }
            maxFreq = max(maxFreq, right - left + 1)
        }
        
        return maxFreq
    }
}
