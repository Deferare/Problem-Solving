class Solution {
    func minimumOperations(_ num: String) -> Int {
        let n = num.count
        var lastZero = -1
        var lastFive = -1
        var result = n
        
        for (index, char) in num.enumerated().reversed() {
            if char == "0" {
                if lastZero != -1 {
                    result = min(result, n - index - 2)
                }
                lastZero = index
            } else if char == "5" {
                if lastZero != -1 {
                    result = min(result, n - index - 2)
                }
                lastFive = index
            } else if char == "2" || char == "7" {
                if lastFive != -1 {
                    result = min(result, n - index - 2)
                }
            }
        }
        
        if lastZero != -1 {
            result = min(result, n - 1)
        }
        
        return result
    }
}
