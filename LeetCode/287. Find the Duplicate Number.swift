class Solution {
func findDuplicate(_ nums: [Int]) -> Int {
    var arr = [Int](repeating: -1, count: nums.count+1)
    for i in 0...nums.count-1 {
        if arr[nums[i]] == 0 {
            return nums[i]
        }
        arr[nums[i]] = 0
    }
    return 0
}
}
