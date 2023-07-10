class Solution {
    func solve(_ board: inout [[Character]]) {
        let m = board.count, n = board[0].count
        
        for i in 0..<n{
            dfs(&board, 0, i)
            dfs(&board, m-1, i)
        }
        
        for i in 0..<m{
            dfs(&board, i, 0)
            dfs(&board, i, n-1)
        }
        
        for i in 0..<m {
            for j in 0..<n {
                if board[i][j] == "O" {
                    board[i][j] = "X"
                }
                else if board[i][j] == "T" {
                    board[i][j] = "O"
                }
            }
        }
    }
    
    private func dfs(_ board: inout [[Character]], _ i: Int, _ j: Int) {
        guard i >= 0, j >= 0, i < board.count, j < board[0].count else { return }
        
        if board[i][j] != "O" {
            return
        }
        
        board[i][j] = "T"
        
        dfs(&board, i + 1, j)
        dfs(&board, i - 1, j)
        dfs(&board, i, j + 1)
        dfs(&board, i, j - 1)
    }
}
