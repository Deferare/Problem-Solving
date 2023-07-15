class Solution {
    func minimumDeletions(_ s: String) -> Int {
        let sArr = Array(s)
        var bCount = 0
        var delections = 0
        
        for char in sArr{
            if char == "b"{
                bCount += 1
            }else if bCount > 0{
                bCount -= 1
                delections += 1
            }
        }
        
        return delections
    }
}
