class Solution {
    func maxJump(_ stones: [Int]) -> Int {
        var minimum = stones[1]
        
        for i in 0..<stones.count-2{
            minimum = max(minimum, stones[i+2] - stones[i])
        }
        
        return minimum
    }
}
