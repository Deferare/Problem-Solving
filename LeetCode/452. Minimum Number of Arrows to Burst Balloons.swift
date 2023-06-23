class Solution {
    func findMinArrowShots(_ points: [[Int]]) -> Int {
        let points = points.sorted{ a,b in
            return a[1] < b[1]
        }
        
        var shotCount = 1
        var lastShotPoint = 0
        for i in 1..<points.count{
            if points[i][0] > points[lastShotPoint][1]{
                shotCount += 1
                lastShotPoint = i
            }
        }
        
        return shotCount
    }
}
