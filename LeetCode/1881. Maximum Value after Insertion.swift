class Solution {
    func maxValue(_ n: String, _ x: Int) -> String {
        let arr = Array(n)
        var maxmized = Array<Character>()
        var isInserted = false
        let isNegative = n.first == "-"
        
        for char in arr {
            if char == "-" {
                maxmized.append(char)
                continue
            }
            
            let num = Int(String(char))!
            
            if !isInserted && ((isNegative && num > x) || (!isNegative && num < x)) {
                maxmized.append(Character(String(x)))
                isInserted = true
            }
            
            maxmized.append(char)
        }
        
        if !isInserted {
            maxmized.append(Character(String(x)))
        }
        
        return String(maxmized)
    }
}
