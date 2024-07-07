class Solution {
    func findSmallestInteger(_ nums: [Int], _ value: Int) -> Int {
        var freq = [Int: Int]()
        var mex = 0
        
        for num in nums {
            let mod = (num % value + value) % value
            freq[mod, default: 0] += 1
        }
        
        while true {
            let mod = mex % value
            if let count = freq[mod], count > 0 {
                freq[mod] = count - 1
            } else {
                break
            }
            
            mex += 1
        }
        
        return mex
    }
}
