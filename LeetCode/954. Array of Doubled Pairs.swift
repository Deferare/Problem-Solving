class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        var countMap = [Int: Int]()
        
        for num in arr {
            countMap[num, default: 0] += 1
        }
        
        let keys = countMap.keys.sorted { abs($0) < abs($1) }
        
        for key in keys {
            if countMap[key] == nil { continue }
            if let doubleCount = countMap[key*2], doubleCount >= countMap[key]! {
                countMap[key*2]! -= countMap[key]!
                if countMap[key*2]! <= 0 {
                    countMap[key*2] = nil
                }
            } else {
                return false
            }
        }
        
        return true
    }
}
