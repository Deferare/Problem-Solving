class Solution {
    func minIncrements(_ n: Int, _ cost: [Int]) -> Int {
        var answer = 0
        var cost = cost
        
        for i in stride(from: n/2-1, through: 0, by: -1){
            let left = 2 * i + 1
            let right = left + 1
            let maxChild = max(cost[left], cost[right])
            
            answer += maxChild - min(cost[left], cost[right])
            cost[i] += maxChild
        }
        
        return answer
    }
}
