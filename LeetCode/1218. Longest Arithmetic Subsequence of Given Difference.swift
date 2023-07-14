class Solution {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        var seqLengths = Dictionary<Int, Int>()
        var maxLength = 0
        
        for num in arr{
            seqLengths[num] = (seqLengths[num - difference] ?? 0) + 1
            maxLength = max(maxLength, seqLengths[num]!)
        }
        
        return maxLength
    }
}
