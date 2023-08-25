class Solution {
    func longestDiverseString(_ a: Int, _ b: Int, _ c: Int) -> String {
        var freq = [(char:"a", count: a), (char: "b", count: b), (char: "c", count: c)]
        var result = [String]()
        
        while true {
            freq.sort { $0.1 > $1.1 }
            
            if let last = result.last, last == freq[0].char{
                if freq[1].count == 0 {break}
                result.append(freq[1].char)
                freq[1].count -= 1
            }else{
                if freq[0].count == 0 {break}
                result.append(freq[0].char)
                if freq[0].count > 1 {
                    result.append(freq[0].char)
                    freq[0].count -= 2
                }else {freq[0].count -= 1}
            }
        }
        
        return result.joined()
    }
}
