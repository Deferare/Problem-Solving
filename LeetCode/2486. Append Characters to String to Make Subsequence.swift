class Solution {
    func appendCharacters(_ s: String, _ t: String) -> Int {
        let s = Array(s)
        let t = Array(t)
        
        var i = 0
        var j = 0
        while i < s.count && j < t.count{
            if s[i] == t[j]{
                j += 1
            }
            i += 1
        }
        
        return t.count - j
    }
}
