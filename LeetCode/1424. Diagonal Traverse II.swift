class Solution {
    func findDiagonalOrder(_ nums: [[Int]]) -> [Int] {
        var diagonals: [Int: [Int]] = [:]
        var maxKey = 0
        
        for i in 0..<nums.count {
            for j in 0..<nums[i].count {
                let key = i + j
                diagonals[key, default: []].append(nums[i][j])
                maxKey = max(maxKey, key)
            }
        }
        
        var result: [Int] = []
        
        for i in 0...maxKey {
            for j in stride(from: diagonals[i]!.count-1, to: -1, by: -1) {
                result.append(diagonals[i]![j])
            }
        }
        
        return result
    }
}
