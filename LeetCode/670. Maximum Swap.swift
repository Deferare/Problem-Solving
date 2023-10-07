class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var digits: [Character] = Array(String(num))
        var lastSeen: [Int] = Array(repeating: 0, count: 10)
        
        for i in 0..<digits.count { lastSeen[Int(String(digits[i]))!] = i }
        for i in 0..<digits.count {
            for digit in stride(from: 9, to: Int(String(digits[i]))!, by: -1) {
                if Int(String(lastSeen[digit]))! > i {
                    digits.swapAt(i, Int(String(lastSeen[digit]))!)
                    return Int(String(digits))!
                }
            }
        }
        
        return num
    }
}
