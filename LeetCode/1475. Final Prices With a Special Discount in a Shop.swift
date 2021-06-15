class Solution {
func finalPrices(_ prices: [Int]) -> [Int] {
    var arr = [Int]()
    for i in 0...prices.count-1 {
        var save = prices[i]
        if i == prices.count-1 {
            arr.append(prices[i])
            break
        }
        for j in i+1...prices.count-1 {
            if prices[j] <= prices[i] {
                save = prices[i] - prices[j]
                break
            }
        }
        arr.append(save)
    }
    return arr
}
}
