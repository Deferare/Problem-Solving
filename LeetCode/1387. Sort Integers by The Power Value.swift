class Solution {
    func getKth(_ lo: Int, _ hi: Int, _ k: Int) -> Int {
        func calculatePower(_ n:Int) -> Int{
            if memo[n] != nil {return memo[n]!}
            var answer = 0
            if n%2 == 0{answer = calculatePower(n / 2) + 1}
            else{answer = calculatePower(n * 3 + 1) + 1}
            memo[n] = answer
            return answer
        }
        var memo = [0:1, 1:0]
        var powerArray = [[Int]]()
        for i in lo...hi{
            powerArray.append([i, calculatePower(i)])
        }
        powerArray.sort {$0[1] < $1[1]}
        return powerArray[k-1][0]
    }
}
