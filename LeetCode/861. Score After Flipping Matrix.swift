class Solution {
    func matrixScore(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var result = m * (1 << (n - 1))
        for i in 1..<n {
            var same = 0
            for j in 0..<m {
                if grid[j][i] == grid[j][0] {
                    same += 1
                }
            }
            result += max(same, m - same) * (1 << (n - i - 1))
        }
        return result
    }
}
