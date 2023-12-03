class Solution {
    func addRungs(_ rungs: [Int], _ dist: Int) -> Int {
        var currentHeight = 0
        var rungsToAdd = 0
        
        for rung in rungs {
            let gap = rung - currentHeight
            
            if gap > dist {
                rungsToAdd += (gap - 1) / dist
            }
            
            currentHeight = rung
        }
        
        return rungsToAdd
    }
}
