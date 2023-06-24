class Solution {
    func calculate(_ s: String) -> Int {
        var result = 0
        var number = 0
        var sign = 1
        var stack = [Int]()
        for c in s {
            if let digit = Int(String(c)) {
                number = number * 10 + digit
            } else if c == "+" {
                result += sign * number
                number = 0
                sign = 1
            } else if c == "-" {
                result += sign * number
                number = 0
                sign = -1
            } else if c == "(" {
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            } else if c == ")" {
                result += sign * number
                number = 0
                sign = stack.removeLast()
                result = stack.removeLast() + sign * result
            }
        }
        
        result += sign * number
        
        return result
    }
}
