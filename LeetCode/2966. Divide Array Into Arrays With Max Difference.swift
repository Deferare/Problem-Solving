class Solution {
    func divideArray(_ nums: [Int], _ k: Int) -> [[Int]] {
        let sorted = nums.sorted()
        var divided = [[Int]]()
        
        for i in stride(from: 0, to: sorted.count, by: 3) {
            if sorted[i + 2] - sorted[i] > k {
                return []
            }
            
            divided.append(Array(sorted[i..<i + 3]))
        }
        
        return divided
    }
}
