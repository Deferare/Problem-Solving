class Solution {
    func minCostToMoveChips(_ position: [Int]) -> Int {
        var n1 = 0; var n2 = 0
        for i in 0..<position.count{
            if position[i]%2 == 0{
                n2 += 1
            }
            else{
                n1 += 1
            }
        }
        return min(n1,n2)
    }
}
