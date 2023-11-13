class Solution {
    func miceAndCheese(_ reward1: [Int], _ reward2: [Int], _ k: Int) -> Int {
        let rewards = zip(reward1, reward2).sorted { $0.0 - $0.1 > $1.0 - $1.1 }
        var answer = 0
        
        for i in 0..<k { answer += rewards[i].0 }
        
        for i in k..<rewards.count { answer += rewards[i].1 }
        
        return answer
    }
}
