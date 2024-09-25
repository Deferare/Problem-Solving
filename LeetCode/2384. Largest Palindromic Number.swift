class Solution {
    func largestPalindromic(_ num: String) -> String {
        var digitCounts: Array<Int> = Array(repeating: 0, count: 10)
        var leftHalf: String = ""
        var center: String = ""
        
        for n in num {
            digitCounts[Int(String(n))!] += 1
        }
        
        for i in (0...9).reversed() {
            if i == 0 && leftHalf.isEmpty {
                continue
            }
            
            leftHalf += String(repeating: Character(String(i)), count: digitCounts[i] / 2)
            digitCounts[i] %= 2
        }
        
        for digit in (0..<digitCounts.count).reversed() where digitCounts[digit] > 0 {
            center = String(digit)
            break
        }
        
        let rightHalf: String = String(leftHalf.reversed())
        
        return leftHalf + center + rightHalf
    }
}
