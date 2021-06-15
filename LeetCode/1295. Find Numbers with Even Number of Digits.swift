class Solution {
func findNumbers(_ nums: [Int]) -> Int {
    var cnt = 0
    for i in 0...nums.count-1 {
        let str = String(nums[i])
        if str.count%2 == 0 {
            cnt += 1
        }
    }
    return cnt
}
}
