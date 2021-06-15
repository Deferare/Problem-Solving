class Solution {
func diagonalSum(_ mat: [[Int]]) -> Int {
    var sum = 0
    for i in 0...mat.count-1 {
        if i != mat.count-i-1 {
            sum += mat[i][i]
            sum += mat[i][mat.count-i-1]
        }
        else {
            sum += mat[i][i]
        }
    }
    return sum
}
}
