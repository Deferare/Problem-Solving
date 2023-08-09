class Solution {
    func largestSubmatrix(_ matrix: [[Int]]) -> Int {
        var compressedMatrix = matrix
        let m = matrix.count
        let n = matrix[0].count
        
        // Compress the matrix by accumulating the values.
        for i in 0..<n{
            var count = 0
            for j in 0..<m{
                count += 1
                if matrix[j][i] == 0{
                    count = 0
                }
                compressedMatrix[j][i] = count
            }
        }
        
        var maxArea = 0
        // Sort each row of the compressed matrix and find the maximum area.
        for i in 0..<m {
            compressedMatrix[i].sort(by: >)
            for j in 0..<n {
                maxArea = max(maxArea, compressedMatrix[i][j] * (j + 1))
            }
        }
        
        return maxArea
    }
}
