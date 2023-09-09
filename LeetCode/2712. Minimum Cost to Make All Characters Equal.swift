class Solution {
    func minimumCost(_ s: String) -> Int {
        let n = s.count
        let s = Array(s)
        
        var prefix = Array(repeating: 0, count: n)
        var suffix = Array(repeating: 0, count: n)
        for i in 1..<n {
            if s[i] == s[i-1] { prefix[i] = prefix[i-1]} else {
                prefix[i] = prefix[i-1] + i
            }
            
            if s[n-i-1] == s[n-i] { suffix[n-i-1] = suffix[n-i]} else {
                suffix[n-i-1] = suffix[n-i] + i
            }
        }
        
        var minimum = Int.max
        for i in 0..<n {
            minimum = min(minimum, prefix[i]+suffix[i])
        }
        
        return minimum
    }
}
