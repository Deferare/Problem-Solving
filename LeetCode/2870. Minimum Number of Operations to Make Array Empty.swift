class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var counter: Dictionary<Int, Int> = [:]
        var operations = 0
        
        for num in nums { counter[num, default: 0] += 1 }
        
        for num in counter.values {
            if num == 1 { return -1 }
            if num%3 != 0 { operations += 1 }
            operations += num/3
        }
        
        return operations
    }
}
