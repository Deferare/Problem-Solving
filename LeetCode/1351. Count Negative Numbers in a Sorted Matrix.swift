class Solution {
func countNegatives(_ grid: [[Int]]) -> Int {
    var check = 0
    for move in grid {
        for move2 in move {
            if move2 < 0 {
                check += 1
            }
        }        
    }
    return check
}
}
