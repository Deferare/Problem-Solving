class Solution {
    func minFlips(_ target: String) -> Int {
        var crntBit:Character = "0"
        var flipCount = 0
        for bit in target{
            if bit != crntBit{
                flipCount += 1
                crntBit = bit
            }
        }
        return flipCount
    }
}
