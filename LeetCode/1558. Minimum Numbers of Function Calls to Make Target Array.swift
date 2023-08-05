class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var maxBits = 0
        var operations = 0
        for num in nums {
            let bits = String(num, radix: 2)
            maxBits = max(maxBits, bits.count)
            operations += bits.filter { $0 == "1" }.count
        }
        return operations + maxBits - 1
    }
}
