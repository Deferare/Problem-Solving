class Solution {
    func stoneGameVI(_ aliceValues: [Int], _ bobValues: [Int]) -> Int {
        var totalValues = aliceValues.indices.map{(aliceValues[$0] + bobValues[$0], $0)}
        totalValues.sort{$0.0 > $1.0}
        var sumScore = 0
        
        for i in 0..<totalValues.count {
            if i%2 == 0 {
                sumScore += aliceValues[totalValues[i].1]
            }else {
                sumScore -= bobValues[totalValues[i].1]
            }
        }
        
        if sumScore > 0 {return 1}
        else if sumScore < 0 {return -1}
        return 0
    }
}
