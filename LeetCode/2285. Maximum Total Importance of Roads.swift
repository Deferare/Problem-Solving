class Solution {
    func maximumImportance(_ n: Int, _ roads: [[Int]]) -> Int {
        var degrees = Array(repeating: 0, count: n)
        
        for road in roads {
            degrees[road[0]] += 1
            degrees[road[1]] += 1
        }
        
        let nodes = (0..<n).sorted(by: { degrees[$0] > degrees[$1] })
        var assignValues = Array(repeating: 0, count: n)
        var value = n, importance = 0
        
        for node in nodes {
            assignValues[node] = value
            value -= 1
        }
        
        for road in roads {
            importance += assignValues[road[0]] + assignValues[road[1]]
        }
        
        return importance
    }
}
