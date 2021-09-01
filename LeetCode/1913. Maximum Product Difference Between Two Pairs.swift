class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let numsLen = nums.count
        return (nums[numsLen-1]*nums[numsLen-2])-(nums[0]*nums[1])
    }
}
