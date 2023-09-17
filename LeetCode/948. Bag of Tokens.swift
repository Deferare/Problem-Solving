class Solution {
    func bagOfTokensScore(_ tokens: [Int], _ power: Int) -> Int {
        let tokens = tokens.sorted()
        var power = power
        var score = 0
        var left = 0, right = tokens.count-1
        
        while left <= right {
            if power >= tokens[left] {
                score += 1
                power -= tokens[left]
                left += 1
            } else if score > 0 && right-1 > left {
                score -= 1
                power += tokens[right]
                right -= 1
            } else { break }
        }
        
        return score
    }
}
