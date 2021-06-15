class Solution {
func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
    func dfs(_ madeArr:[Int],_ sum:Int,_ index:Int) {
        var madeArr = madeArr
        var sum = sum
        madeArr.append(candidates[index])
        sum += candidates[index]
        if sum == target {
            result.append(madeArr)
            return
        }
        
        else if sum > target {
            return
        }
        
        for i in index...candidates.count-1 {
            dfs(madeArr, sum, i)
        }
    }
    var result = [[Int]]()
    for i in 0...candidates.count-1 {
        dfs([Int](), 0, i)
    }
    return result
}
}
