class Solution {
    func groupThePeople(_ groupSizes: [Int]) -> [[Int]] {
        var contain = Dictionary<Int,Array<Int>>()
        var resultArr = [Array<Int>]()
        for i in 0..<groupSizes.count{
            if contain[groupSizes[i]] == nil{
                contain[groupSizes[i]] = [i]
            }
            else{
                contain[groupSizes[i]]?.append(i)
            }
            if contain[groupSizes[i]]?.count == groupSizes[i]{
                resultArr.append(contain[groupSizes[i]]!)
                contain[groupSizes[i]] = nil
            }
        }
        return resultArr
    }
}
