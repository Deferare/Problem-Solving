class Solution {
    func minFlips(_ s: String) -> Int {
        let n = s.count
        var pattern1: [Character] = Array(repeating: "0", count: n * 2)
        var pattern2: [Character] = Array(repeating: "1", count: n * 2)
        
        for i in stride(from: 1, to: n * 2, by: +2) {
            pattern1[i] = "1"
            pattern2[i] = "0"
        }
        
        let sArr = Array(s) + Array(s)
        var flips1 = 0
        var flips2 = 0
        
        for i in 0..<n {
            if sArr[i] != pattern1[i] {
                flips1 += 1
            }
            if sArr[i] != pattern2[i] {
                flips2 += 1
            }
        }
        
        var result = min(flips1, flips2)
        
        for i in 1..<n {
            if sArr[i - 1] != pattern1[i - 1] {
                flips1 -= 1
            }
            if sArr[i - 1] != pattern2[i - 1] {
                flips2 -= 1
            }

            if sArr[i + n - 1] != pattern1[i + n - 1] {
                flips1 += 1
            }
            if sArr[i + n - 1] != pattern2[i + n - 1] {
                flips2 += 1
            }
            
            result = min(result, min(flips1, flips2))
        }
        
        return result
    }
}
