class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
        func checkCircuit(_ startIndOrigin:Int) -> Bool{
            var check = true
            var accumGas = 0
            for j in startIndOrigin..<lenth+startIndOrigin{
                var indJ = j
                if indJ >= lenth{
                    indJ = indJ - lenth
                }
                check = true
                accumGas += (gas[indJ] - cost[indJ])
                if accumGas < 0 {
                    check = false
                    start = j+1
                    break
                }
            }
            return check
        }
        let lenth = gas.count
        var start = 0
        while checkCircuit(start) == false{
            if start >= lenth{
                return -1
            }
        }
        return start != -1 ? start : -1
    }
}
