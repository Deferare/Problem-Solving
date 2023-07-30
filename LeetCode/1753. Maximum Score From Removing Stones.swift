class Solution {
    func maximumScore(_ a: Int, _ b: Int, _ c: Int) -> Int {
        var score = 0
        var piles = [a,b,c]
        
        while true{
            piles.sort(by: >)
            if piles[1] < 1 {break}
            piles[0] -= 1
            piles[1] -= 1
            score += 1
        }
        
        return score
    }
}
