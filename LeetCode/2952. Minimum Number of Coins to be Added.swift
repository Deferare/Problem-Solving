class Solution {
    func minimumAddedCoins(_ coins: [Int], _ target: Int) -> Int {
        let sortedCoins = coins.sorted()
        var addedCount = 0
        var currentMax = 0
        var i = 0
        
        while currentMax < target {
            if i < sortedCoins.count && sortedCoins[i] <= currentMax + 1 {
                currentMax += sortedCoins[i]
                i += 1
            } else {
                currentMax += currentMax + 1
                addedCount += 1
            }
        }
        
        return addedCount
    }
}
