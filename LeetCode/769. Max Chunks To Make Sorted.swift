class Solution {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        var splitedCount = 0
        var maxSoFar = 0
        
        for i in 0..<arr.count{
            maxSoFar = max(maxSoFar, arr[i])
            if i == maxSoFar{
                splitedCount += 1
            }
        }
        
        return splitedCount
    }
}
