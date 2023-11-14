class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        let s = Array(s)
        var indices: Dictionary<Character, (first: Int, last: Int)> = [:]
        var pCount = 0
        
        for (index, char) in s.enumerated() {
            if indices[char] == nil {
                indices[char] = (index, index)
            } else {
                indices[char]!.last = index
            }
        }
        
        for value in indices.values {
            if value.first != value.last {
                pCount += Set(s[value.first+1..<value.last]).count
            }
        }
        
        return pCount
    }
}
