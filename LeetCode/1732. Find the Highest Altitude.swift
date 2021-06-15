class Solution {
func largestAltitude(_ gain: [Int]) -> Int {
    var alititude = gain[0]
    var max = alititude
    if gain.count > 1 {
        for i in 1...gain.count-1 {
            alititude = alititude + gain[i]
            if alititude > max {
                max = alititude
            }
        }
    }
    if max < 0 {
        return 0
    }
    return max
}
}
