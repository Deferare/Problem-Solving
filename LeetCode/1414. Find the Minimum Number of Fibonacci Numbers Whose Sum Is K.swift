class Solution {
    func findMinFibonacciNumbers(_ k: Int) -> Int {
        var fibonacciArr = [1, 1]
        var i = 1
        
        while fibonacciArr.last ?? 0 < k{
            fibonacciArr.append(fibonacciArr[i] + fibonacciArr[i-1])
            i += 1
        }
        
        var count = 0
        var remaining = k
        
        for i in stride(from: fibonacciArr.count-1, through: 0, by: -1){
            if fibonacciArr[i] <= remaining{
                count += 1
                remaining -= fibonacciArr[i]
            }
        }
        
        return count
    }
}
