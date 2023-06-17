class Solution {
    func numSplits(_ s: String) -> Int {
        let sArray = Array(s)
        let len = sArray.count
        var leftNumbers = [Int]()
        var rightNumbers = [Int]()
        
        var leftSet = Set<Character>()
        var rightSet = Set<Character>()
        
        for i in 0..<len{
            leftSet.insert(sArray[i])
            leftNumbers.append(leftSet.count)
            rightSet.insert(sArray[len-i-1])
            rightNumbers.append(rightSet.count)
        }
        
        var count = 0
        for i in 0..<len-1{
            if leftNumbers[i] == rightNumbers[len-2-i] {count += 1}
        }

        return count
    }
}
