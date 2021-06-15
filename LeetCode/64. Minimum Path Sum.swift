class Solution {
func minPathSum(_ grid: [[Int]]) -> Int {
    var memo = [Array](repeating: [Int](repeating: -1, count: grid[0].count), count: grid.count)
    func dp(grid:[[Int]],i:Int, j:Int) -> Int {
        if i > grid.count-1 || j > grid[i].count-1 {
            return 0
        }
        if memo[i][j] != -1 {
            return memo[i][j]
        }
        if i == grid.count-1 {
            return dp(grid: grid, i: i, j: j+1) + grid[i][j]
        }
        if j == grid[i].count-1 {
            return dp(grid: grid, i: i+1, j: j) + grid[i][j]
        }
        if i == grid.count-1 && j == grid[i].count-1 {
            return grid[i][j]
        }
        memo[i][j] = min(dp(grid: grid, i: i, j: j+1), dp(grid: grid, i: i+1, j: j)) + grid[i][j]
        return memo[i][j]
    }
    let value = dp(grid: grid, i: 0, j: 0)
    return value
}
}
