class Solution {
    func addMinimum(_ word: String) -> Int {
        let word = Array(word)
        let pattern: [Character] = ["a", "b", "c"]
        var count = 0, i = 0
        
        while i < word.count {
            for p in pattern {
                if i < word.count && word[i] == p {
                    i += 1
                } else {
                    count += 1
                }
            }
        }
        
        return count
    }
}
