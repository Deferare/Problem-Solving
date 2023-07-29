class Solution {
    func maximumGroups(_ grades: [Int]) -> Int {
        let grades = grades.sorted()
        var groupCount = 0
        var preCount = 0
        var preSum = 0
        var crntCount = 0
        var crntSum = 0
        
        for grade in grades{
            crntCount += 1
            crntSum += grade
            
            if crntCount > preCount && crntSum > preSum{
                groupCount += 1
                preCount = crntCount
                preSum = crntSum
                crntCount = 0
                crntSum = 0
            }
        }
        
        return groupCount
    }
}
