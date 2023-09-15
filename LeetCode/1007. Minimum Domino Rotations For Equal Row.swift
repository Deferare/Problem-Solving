class Solution {
    func minDominoRotations(_ tops: [Int], _ bottoms: [Int]) -> Int {
        var tops = tops
        var bottoms = bottoms
        let a = self.check(tops[0], &tops, &bottoms)
        let b = self.check(tops[0], &bottoms, &tops)
        let c = self.check(bottoms[0], &bottoms, &tops)
        let d = self.check(bottoms[0], &tops, &bottoms)
        
        var result = Int.max
        for rotation in [a, b, c, d] {
            if rotation != -1 {
                result = min(result, rotation)
            }
        }
        
        return result != Int.max ? result : -1
    }
    
    private func check(_ target: Int, _ tops: inout [Int], _ bottoms: inout [Int]) -> Int {
        var rotations = 0
        for i in 0..<tops.count {
            if tops[i] != target {
                if bottoms[i] == target { rotations += 1 }
                else { return -1 }
            }
        }
        
        return rotations
    }
}
