class Solution {
    func getAverages(_ nums: [Int], _ k: Int) -> [Int] {
        if k == 0 { return nums }
        if nums.count < (k*2)+1 { return Array(repeating: -1, count: nums.count) }

        var result = Array(repeating: -1, count: nums.count), crntSum = 0
        let range = (k*2)+1
        
        for i in 0...k*2 { crntSum += nums[i] }
        result[k] = crntSum/range
        
        for i in k+1..<nums.count-k {
            crntSum -= nums[i-k-1]
            crntSum += nums[i+k]
            result[i] = crntSum/range
        }
        
        return result
    }
}
