class Solution {
    func maximumGain(_ s: String, _ x: Int, _ y: Int) -> Int {
        var stack: [Character] = [], stack2: [Character] = []
        let high: (Character, Character, Int) = x > y ? ("a", "b", x) : ("b", "a", y)
        let low: (Character, Character, Int) = x > y ? ("b", "a", y) : ("a", "b", x)
        var points = 0
        
        for char in s {
            if !stack.isEmpty && stack.last! == high.0 && char == high.1 {
                stack.removeLast()
                points += high.2
                
            } else { stack.append(char) }
        }
        
        for char in stack {
            if !stack2.isEmpty && stack2.last! == low.0 && char == low.1 {
                stack2.removeLast()
                points += low.2
                
            } else { stack2.append(char) }
        }
        
        return points
    }
}
