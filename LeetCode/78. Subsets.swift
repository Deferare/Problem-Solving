class Solution {
func subsets(_ nums: [Int]) -> [[Int]] {
    var result = [[Int]]()
    func dfs(_ arr:[Int],_ index:Int) {
        if index >= nums.count {
            return
        }
        var arr = arr
        arr.append(nums[index])
        result.append(arr)
        for i in index...nums.count-1 {
            dfs(arr, i+1)
        }
        arr.removeAll()
    }
    var arr = [Int]()
    for i in 0...nums.count-1 {
        dfs(arr, i)
    }
    result.append([])
    return result
}
}
