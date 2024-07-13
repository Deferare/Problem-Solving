class Solution {
    func maxSumRangeQuery(_ nums: [Int], _ requests: [[Int]]) -> Int {
        let n = nums.count
        var freq = Array(repeating: 0, count: n)
        
        for request in requests {
            freq[request[0]] += 1
            if request[1] + 1 < n {
                freq[request[1] + 1] -= 1
            }
        }
        
        for i in 1..<n {
            freq[i] += freq[i - 1]
        }
        
        let sortedFreq = freq.sorted(by: >)
        let sortedNums = nums.sorted(by: >)
        
        var maxSum = 0
        
        for i in 0..<n {
            maxSum += sortedFreq[i] * sortedNums[i]
        }
        
        return maxSum % 1000000007
    }
}
