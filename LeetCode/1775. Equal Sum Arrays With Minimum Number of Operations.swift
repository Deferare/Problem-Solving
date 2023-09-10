class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var diff = 0
        for num in nums1 {
            diff += num
        }
        for num in nums2 {
            diff -= num
        }
        
        var numsA:[Int] = []
        var numsB:[Int] = []
        
        if diff > 0 {
            numsA = nums1.sorted(by: >)
            numsB = nums2.sorted(by: <)
        } else {
            numsA = nums2.sorted(by: >)
            numsB = nums1.sorted(by: <)
        }
        
        var operCount = 0
        diff = abs(diff)
        
        var (inxA, inxB) = (0,0)
        
        while diff > 0 {
            if inxA < numsA.count && inxB < numsB.count {
                if 7 - numsA[inxA] <= numsB[inxB] {
                    diff -= numsA[inxA] - 1
                    inxA += 1
                } else {
                    diff -= 6 - numsB[inxB]
                    inxB += 1
                }
            } else if inxA < numsA.count {
                diff -= numsA[inxA] - 1
                inxA += 1
            } else if inxB < numsB.count {
                diff -= 6 - numsB[inxB]
                inxB += 1
            } else { return -1 }
            operCount += 1
        }
        
        return operCount
    }
}
