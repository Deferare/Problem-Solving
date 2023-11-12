class Solution {
    func strWithout3a3b(_ a: Int, _ b: Int) -> String {
        var result = ""
        var a = a, b = b
        
        while a > 0 || b > 0 {
            let writeA = (a >= b && result.suffix(2) != "aa") || result.suffix(2) == "bb"
            
            if writeA && a > 0 {
                result += "a"
                a -= 1
            } else if b > 0 {
                result += "b"
                b -= 1
            }
        }
        
        return result
    }
}
