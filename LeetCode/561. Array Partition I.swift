class Solution {
    func arrayPairSum(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var result_sum = 0
        for i in stride(from: nums.count-2, to: -1, by: -2){
            result_sum += nums[i]
        }
        return result_sum
    }
}
