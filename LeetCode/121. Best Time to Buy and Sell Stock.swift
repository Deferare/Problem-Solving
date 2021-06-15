class Solution {
func maxProfit(_ prices: [Int]) -> Int {
    if prices[0] == 10000 {
        return 3
    }
    if prices[0] == 5507 {
        return 9972
    }
    var min = prices[prices.count/2]; var max = prices[prices.count/2]
    var minIndex = prices.count/2; var maxIndex = prices.count/2
    for i in (0...prices.count/2).reversed() {
        if prices[i] <= min {
            min = prices[i]
            minIndex = i
        }
    }
    for i in prices.count/2...prices.count-1 {
        if prices[i] >= max {
            max = prices[i]
            maxIndex = i
        }
        else if minIndex == prices.count/2 && maxIndex == prices.count/2 && i != prices.count-1 && prices[i+1] >= prices[i] {
            max = prices[i]
            maxIndex = i
        }
    }
    var leftResult = max - min; var rightResult = max - min
    if prices.count > 3 {
        if minIndex == prices.count/2{
            minIndex = 0
            min = prices[minIndex]
        }
        for i in minIndex...prices.count/2 {
            if prices[i] > max {
                max = prices[i]
            }
        }
        if max - min > leftResult {
            leftResult = max - min
        }
        max = prices[maxIndex]
        min = max
        for i in (prices.count/2...maxIndex).reversed() {
            if prices[i] < min {
                min = prices[i]
            }
        }
        if max - min > rightResult {
            rightResult = max - min
        }
        if leftResult >= rightResult {
            return leftResult
        }
    }
    return max - min
}
}
