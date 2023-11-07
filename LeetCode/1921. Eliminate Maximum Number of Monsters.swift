class Solution {
    func eliminateMaximum(_ dist: [Int], _ speed: [Int]) -> Int {
        let times = zip(dist, speed).map { $0 / $1 + ($0 % $1 != 0 ? 1 : 0) }.sorted()
        
        for (i, time) in times.enumerated() {
            if time <= i {
                return i
            }
        }
        
        return times.count
    }
}
