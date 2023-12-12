class Solution {
    func removeAlmostEqualCharacters(_ word: String) -> Int {
        let converted: [Int] = word.unicodeScalars.map {Int($0.value)}
        var result = 0
        var i = 1
        
        while i < converted.count {
            if abs(converted[i-1] - converted[i]) <= 1 {
                result += 1
                i += 2
            } else {
                i += 1
            }
        }
        
        return result
    }
}
