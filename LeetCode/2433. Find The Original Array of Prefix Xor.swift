class Solution {
    func findArray(_ pref: [Int]) -> [Int] {
        var answer = [pref.first!]
        
        for i in 1..<pref.count {
            answer.append(pref[i-1] ^ pref[i])
        }
        
        return answer
    }
}
