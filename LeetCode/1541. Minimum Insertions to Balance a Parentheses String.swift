class Solution {
    func minInsertions(_ s: String) -> Int {
        let s = Array(s)
        var res = 0, left = 0
        var i = 0
        
        while i < s.count {
            if s[i] == "(" { left += 1 }
            else {
                if left > 0 { left -= 1 }
                else { res += 1 }
                if i < s.count-1 && s[i+1] == ")" { i += 1 }
                else { res += 1 }
            }
            
            i += 1
        }
        
        return res + left * 2
    }
}
