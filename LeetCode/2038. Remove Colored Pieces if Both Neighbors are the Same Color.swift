class Solution {
    func winnerOfGame(_ colors: String) -> Bool {
        var score = 0
        var state = 0
        
        for color in colors {
            if color == "A" && state >= 0 { state += 1 }
            else if color == "B" && state <= 0 { state -= 1 }
            else if color == "A" { state = 1 }
            else { state = -1 }
            
            if state >= 3 { score += 1 }
            else if state <= -3 { score -= 1 }
        }
        
        return score >= 1
    }
}
