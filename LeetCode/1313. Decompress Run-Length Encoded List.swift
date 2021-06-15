class Solution {
func decompressRLElist(_ nums: [Int]) -> [Int] {
    var result = [Int]()
    var index = 0
    while index < nums.count-1 {
        for j in 0...nums[index]-1 {
            result.append(nums[index+1])
        }
        index += 2
    }
    return result
}
}
