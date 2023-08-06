class Solution {
    func minimumRounds(_ tasks: [Int]) -> Int {
        var freq: [Int: Int] = [:]
        for task in tasks {
            freq[task, default: 0] += 1
        }
        
        var rounds = 0
        
        for (_, count) in freq {
            if count == 1 {return -1}
            
            rounds += (count + 2) / 3
        }
        
        return rounds
    }
}
