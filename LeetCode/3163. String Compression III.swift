class Solution {
    func compressedString(_ word: String) -> String {
        var comp = ""
        var crntIndex = word.startIndex
        
        while crntIndex < word.endIndex {
            let crntChar = word[crntIndex]
            var crntCount = 0
            
            while crntIndex < word.endIndex, crntCount < 9, crntChar == word[crntIndex] {
                crntCount += 1
                crntIndex = word.index(after: crntIndex)
            }
            
            comp += "\(crntCount)\(crntChar)"
        }
        
        return comp
    }
}
