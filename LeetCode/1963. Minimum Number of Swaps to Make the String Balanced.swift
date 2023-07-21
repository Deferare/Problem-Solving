class Solution {
    func minSwaps(_ s: String) -> Int {
        var swapCount = 0
        var leftCount = 0
        
        for c in s{
            if c == "]" {leftCount -= 1}
            else{ leftCount += 1 }
            if leftCount < 0{
                swapCount += 1
                leftCount = 0
            }
        }
        
        return (swapCount + 1)/2
    }
}
