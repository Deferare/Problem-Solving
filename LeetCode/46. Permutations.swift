class Solution {
func permute(_ nums: [Int]) -> [[Int]] {
    var result = [[Int]]()
    func dfs(_ nums:[Int],_ made:[Int],_ index:Int) {
        if index == nums.count {
            result.append(made)
            return
        }
        var nums = nums; var made = made
        for i in 0...nums.count-1 {
            if nums[i] == -11 {
                continue
            }
            made[index] = nums[i]
            nums[i] = -11
            dfs(nums, made, index+1)
            nums[i] = made[index]
        }
    }
    dfs(nums, [Int](repeating: 0, count: nums.count), 0)
    return result
}
}
