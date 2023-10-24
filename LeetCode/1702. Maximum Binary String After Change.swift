class Solution {
    func maximumBinaryString(_ binary: String) -> String {
        var zeroCount = 0
        var firstZeroPos = -1
        for (i, char) in binary.enumerated() {
            if char == "0" {
                zeroCount += 1
                if firstZeroPos == -1 {
                    firstZeroPos = i
                }
            }
        }
        
        if zeroCount <= 1 { return binary }
        
        var result = Array(repeating: "1", count: binary.count)
        result[firstZeroPos+zeroCount-1] = "0"
        
        return result.joined()
    }
}
