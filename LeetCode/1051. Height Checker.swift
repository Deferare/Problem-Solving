class Solution {
    func heightChecker(_ heights: [Int]) -> Int {
        let heightsSort = heights.sorted()
        var resultCnt = 0
        for i in 0..<heights.count{
            if heights[i] != heightsSort[i]{
                resultCnt += 1
            }
        }
        return resultCnt
    }
}
