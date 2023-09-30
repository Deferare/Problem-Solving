class Solution {
    func minSideJumps(_ obstacles: [Int]) -> Int {
        var nextObs = (one: Int.max, two: Int.max, three: Int.max)
        var jumps = 0, lane = 2
        
        for i in 0..<obstacles.count-1 {
            if obstacles[i+1] != lane { continue }
            else {
                var (a, b, c) = (Int.max, Int.max, Int.max)
                for i in i..<obstacles.count {
                    if a != Int.max && b != Int.max && c != Int.max { break }
                    if a == Int.max && obstacles[i] == 1 { a = i }
                    else if b == Int.max && obstacles[i] == 2 { b = i }
                    else if c == Int.max && obstacles[i] == 3 { c = i }
                }
                nextObs = (a, b, c)
            }
            
            if nextObs.one >= nextObs.two && nextObs.one >= nextObs.three { lane = 1 }
            else if nextObs.two >= nextObs.one && nextObs.two >= nextObs.three { lane = 2 }
            else { lane = 3 }
            jumps += 1
        }
        
        return jumps
    }
}
