class Solution {
    func smallestSubsequence(_ s: String) -> String {
        var result = [Character]()
        var lastOccurrence = [Character:Int]()
        var seen = [Character:Bool]()
        
        for (i, char) in s.enumerated(){
            lastOccurrence[char] = i
        }
        
        for (i, char) in s.enumerated(){
            if seen[char] == nil{
                while let last = result.last, last > char, lastOccurrence[last]! > i{
                    seen[last] = nil
                    let _ = result.removeLast()
                }
                seen[char] = true
                result.append(char)
            }
        }
        
        return String(result)
    }
}
