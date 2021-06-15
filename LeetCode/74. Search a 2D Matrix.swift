class Solution {
func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
    var i = 0; var j = 0
    while true {
        if matrix[i][j] == target {
            return true
        }
        else {
            if matrix.count-1 > i && matrix[i+1][j] <= target {
                i += 1
            }
            else if matrix.count-1 > i && matrix[i].count-1 == j{
                i += 1
            }
            else if matrix[i].count-1 > j && matrix[i][j+1] <= target {
                j += 1
            }
            else if matrix[i].count-1 > j && matrix[i][j+1] > target {
                return false
            }
            if matrix[i][j] == target {
                return true
            }
            if i == matrix.count-1 && j == matrix[i].count-1{
                return false
            }
        }
    }
}
}
