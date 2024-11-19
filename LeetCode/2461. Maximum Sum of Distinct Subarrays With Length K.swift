class Solution {
    func maximumSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        var crntSum = 0
        var maxSum = 0
        var uniqueElements: Set<Int> = []
        var left = 0
        
        for right in 0..<nums.count {
            while uniqueElements.contains(nums[right]) || right - left + 1 > k {
                uniqueElements.remove(nums[left])
                crntSum -= nums[left]
                left += 1
            }
            
            uniqueElements.insert(nums[right])
            crntSum += nums[right]
            
            if right - left + 1 == k {
                maxSum = max(maxSum, crntSum)
            }
        }
        
        return maxSum
    }
}
