class Solution {
    func isPossibleDivide(_ nums: [Int], _ k: Int) -> Bool {
        if nums.count%k != 0 {return false}
        if k == 1 {return true}
        
        var counter = Dictionary<Int, Int>()
        for num in nums {counter[num, default: 0] += 1}
            
        let nums = nums.sorted()
        
        for num in nums {
            if counter[num] == 0 {continue}
            for i in num..<num+k {
                if counter[i] == nil || counter[i] == 0 {return false}
                counter[i]! -= 1
            }
        }
        
        return true
    }
}
