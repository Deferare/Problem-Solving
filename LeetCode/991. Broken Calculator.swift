class Solution {
    func brokenCalc(_ startValue: Int, _ target: Int) -> Int {
        var startValue = startValue
        var target = target
        var ops = 0
        
        while startValue < target {
            ops += 1
            if target % 2 == 1 {
                target += 1
            } else {
                target /= 2
            }
        }
        
        return ops + startValue - target
    }
}
