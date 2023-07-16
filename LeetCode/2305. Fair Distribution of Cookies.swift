class Solution {
    func distributeCookies(_ cookies: [Int], _ k: Int) -> Int {
        func dfs(_ index: Int) {
            if index == cookies.count {
                minUnfairness = min(minUnfairness, count.max() ?? 0)
                return
            }
            
            var used = Set<Int>()
            for i in 0..<k {
                if used.contains(count[i]) { continue }
                used.insert(count[i])
                
                count[i] += cookies[index]
                dfs(index + 1)
                count[i] -= cookies[index]
            }
        }
        
        var count = Array(repeating: 0, count: k)
        var minUnfairness = Int.max
        dfs(0)
        
        return minUnfairness
    }
}
