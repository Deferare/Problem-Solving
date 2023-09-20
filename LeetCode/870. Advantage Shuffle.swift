class Solution {
    func advantageCount(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let sortedNums1 = nums1.sorted()
        var sortedNums2 = nums2.enumerated().sorted(by: {$0.element < $1.element})
        var result: [Int] = Array(repeating: 0, count: nums1.count)
        var i = 0
        
        for num in sortedNums1 {
            if num > sortedNums2[i].element {
                result[sortedNums2[i].offset] = num
                i += 1
            } else {
                let last = sortedNums2.removeLast()
                result[last.offset] = num
            }
        }
        
        return result
    }
}
