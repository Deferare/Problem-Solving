class Solution {
    func getMaximumConsecutive(_ coins: [Int]) -> Int {
        let sorted = coins.sorted()
        var crntSum = 0
        
        for coin in sorted {
            if coin > crntSum + 1 {break}
            crntSum += coin
        }
        
        return crntSum + 1
    }
}
