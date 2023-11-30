class Solution {
    func minimumSteps(_ s: String) -> Int {
        var result = 0
        var oneCount = 0
        
        for char in s {
            if char == "1" {
                oneCount += 1
            } else {
                result += oneCount
            }
        }
        
        return result
    }
}
