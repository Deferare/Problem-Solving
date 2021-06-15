class Solution {
func shuffle(_ nums: [Int], _ n: Int) -> [Int] {
    var result = [Int](repeating: 0, count: nums.count)
    var firstIndex = 0
    var endIndex = n
    for i in 0...nums.count/2-1 {
        result[firstIndex] = nums[i]
        result[firstIndex+1] = nums[endIndex]
        firstIndex += 2
        endIndex += 1
    }
    return result
}
}
