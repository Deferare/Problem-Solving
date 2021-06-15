class Solution {
func generateParenthesis(_ n: Int) -> [String] {
    func dfs(_ madeStr:String,_ open:Int,_ close:Int) {
        if open == 0 && close == 0 {
            result.append(madeStr)
            return
        }
        if open == 0 && close > 0 {
            var madeStr = madeStr
            madeStr.append(")")
            dfs(madeStr, open, close-1)
            return
        }
        if close-1 < open {
            var madeStr = madeStr
            madeStr.append("(")
            dfs(madeStr, open-1, close)
            return
        }
        else {
            var madeStr = madeStr
            madeStr.append(")")
            dfs(madeStr, open, close-1)
            madeStr.removeLast()
            madeStr.append("(")
            dfs(madeStr, open-1, close)
        }
    }
    var result = [String]()
    dfs(String(), n, n)
    return result
}
}
