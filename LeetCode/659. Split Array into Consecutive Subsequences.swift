class Solution {
    func isPossible(_ nums: [Int]) -> Bool {
        var count = [Int: Int]()
        var tails = [Int: Int]()
        
        for num in nums {
            count[num, default: 0] += 1
        }
        
        for num in nums {
            if count[num] == 0 { continue }
            else if let v = tails[num-1], v > 0 {
                tails[num-1]! -= 1
                tails[num, default: 0] += 1
            } else if let v1 = count[num+1], v1 > 0, let v2 =  count[num+2], v2 > 0 {
                tails[num+2, default: 0] += 1
                count[num+1]! -= 1
                count[num+2]! -= 1
            } else { return false }
            
            count[num]! -= 1
        }
        
        return true
    }
}
