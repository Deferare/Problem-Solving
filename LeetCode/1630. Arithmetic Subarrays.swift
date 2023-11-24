class Solution {
    func checkArithmeticSubarrays(_ nums: [Int], _ l: [Int], _ r: [Int]) -> [Bool] {
        var result: [Bool] = []

        for i in 0..<l.count {
            let subarray = Array(nums[l[i]...r[i]]).sorted()
            let diff = subarray[1] - subarray[0]
            var isArithmetic = true
            
            for j in 1..<subarray.count {
                if subarray[j] - subarray[j - 1] != diff {
                    isArithmetic = false
                    break
                }
            }
            
            result.append(isArithmetic)
        }
        
        return result
    }
}
