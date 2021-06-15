class Solution {
func maximumWealth(_ accounts: [[Int]]) -> Int {
    var sum = accounts[0][0]
    for i in 0...accounts.count-1 {
        var saveN = 0
        for j in 0...accounts[i].count-1 {
            saveN += accounts[i][j]
        }
        if saveN > sum {
            sum = saveN
        }
    }
    return sum
}
}
