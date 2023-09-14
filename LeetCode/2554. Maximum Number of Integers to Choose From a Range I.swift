class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
        let banned = Set(banned)
        var addedCount = 0
        var addedSum = 0
        
        for i in 1...n {
            if addedSum + i > maxSum { break }
            if !banned.contains(i) {
                addedCount += 1
                addedSum += i
            }
        }
        
        return addedCount
    }
}
