class Solution {
    func findLeastNumOfUniqueInts(_ arr: [Int], _ k: Int) -> Int {
        var counter = Dictionary<Int, Int>()
        for n in arr {counter[n, default: 0] += 1}
        let sorted = counter.sorted(by: {$0.value < $1.value})
        
        var result = sorted.count
        var k = k
        
        for pair in sorted {
            if pair.value <= k {
                result -= 1
                k -= pair.value
            } else {break}
        }
        
        return result
    }
}
