class Solution {
func flipAndInvertImage(_ image: [[Int]]) -> [[Int]] {
    var matrix = [[Int]]()
    for i in 0...image.count-1 {
        var saveN = [Int]()
        for j in (0...image[i].count-1).reversed() {
            saveN.append(image[i][j])
        }
        matrix.append(saveN)
    }
    for i in 0...matrix.count-1 {
        for j in 0...matrix[i].count-1 {
            if matrix[i][j] == 0 {
                matrix[i][j] = 1
            }
            else {
                matrix[i][j] = 0
            }
        }
    }
    return matrix
}
}
