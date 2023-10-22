class Solution {
    func minSwaps(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var zeroes = [Int](repeating: 0, count: n)
        for i in 0..<n {
            for j in stride(from: n-1, to: -1, by: -1) {
                if grid[i][j] == 0 {
                    zeroes[i] += 1
                } else { break }
            }
        }
        
        var swaps = 0
        for i in 0..<n {
            var ok = false
            for j in i..<n {
                if zeroes[j] >= n-i-1 {
                    zeroes.remove(at: j)
                    zeroes.insert(i, at: i)
                    swaps += j-i
                    ok = true
                    break
                }
            }
            if !ok { return -1 }
        }
        
        return swaps
    }
}
