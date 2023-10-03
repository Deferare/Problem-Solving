class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        let nums = nums.sorted()
        var result: [Int] = []
        var i = 0, j = nums.count-1
        
        while i < j {
            result += [nums[i], nums[j]]
            i += 1
            j -= 1
        }
        
        if i == j { result.append(nums[i]) }
        
        return result
    }
}
