class Solution {
    func maxValue(_ n: Int, _ index: Int, _ maxSum: Int) -> Int {
        func sumOfFirstK(_ k: Int) -> Int {
            return k * (k + 1) / 2
        }
        
        func sumWithPeak(_ peak: Int,_ length: Int) -> Int {
            if length >= peak {
                return sumOfFirstK(peak) + (length - peak)
            } else {
                return sumOfFirstK(peak) - sumOfFirstK(peak - length)
            }
        }
        
        var left = 1
        var right = maxSum
        
        while left < right {
            let mid = (left + right + 1) / 2
            
            let leftSum = sumWithPeak(mid - 1, index)
            let rightSum = sumWithPeak(mid - 1, n - index - 1)
            let totalSum = leftSum + mid + rightSum
            
            if totalSum <= maxSum {
                left = mid
            } else {
                right = mid - 1
            }
        }
        
        return left
    }
}
