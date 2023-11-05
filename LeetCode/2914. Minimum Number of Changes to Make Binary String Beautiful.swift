class Solution {
    func minChanges(_ s: String) -> Int {
        let s = Array(s)
        var count = 0
        
        for i in stride(from: 1, to: s.count, by: 2) {
            if s[i] != s[i-1] { count += 1 }
        }
        
        return count
    }
}
