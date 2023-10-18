class Solution {
    func largestMerge(_ word1: String, _ word2: String) -> String {
        var word1 = Array(word1), word2 = Array(word2)
        var merge = ""
        
        while !word1.isEmpty || !word2.isEmpty {
            if word1.lexicographicallyPrecedes(word2) {
                merge.append(word2.removeFirst())
            } else {
                merge.append(word1.removeFirst())
            }
        }
        
        return merge
    }
}
