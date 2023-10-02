class Solution {
    func minMoves(_ target: Int, _ maxDoubles: Int) -> Int {
        var target = target
        var maxDoubles = maxDoubles
        var count = 0
        
        while target != 1 {
            if maxDoubles == 0 {
                count += target-1
                return count
            }
            
            if target.isMultiple(of: 2) {
                target /= 2
                maxDoubles -= 1
            } else { target -= 1 }
            
            count += 1
        }
        
        return count
    }
}
