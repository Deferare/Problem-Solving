class Solution {
    func getWordsInLongestSubsequence(_ n: Int, _ words: [String], _ groups: [Int]) -> [String] {
        var answer: [String] = [words[0]]
        
        for i in 1..<n {
            if groups[i] != groups[i-1] {
                answer.append(words[i])
            }
        }
        
        return answer
    }
}
