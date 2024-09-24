class Solution {
    func minSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let numsA = calculateSumAndZeros(nums1)
        let numsB = calculateSumAndZeros(nums2)
        
        let minSumA = numsA.sum + numsA.zeros
        let minSumB = numsB.sum + numsB.zeros
        
        if numsA.zeros == 0 && numsB.zeros == 0 {
            if numsA.sum != numsB.sum {
                return -1
            }
        }
        
        if numsA.zeros == 0 && minSumA < minSumB {
            return -1
        }
        
        if numsB.zeros == 0 && minSumB < minSumA {
            return -1
        }
        
        return max(minSumA, minSumB)
    }
    
    private func calculateSumAndZeros(_ nums: [Int]) -> (sum: Int, zeros: Int) {
        nums.reduce(into: (0, 0)) { result, num in
            if num == 0 {
                result.1 += 1
            }
            
            result.0 += num
        }
    }
}
