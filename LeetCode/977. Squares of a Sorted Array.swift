class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        var tranNums = [Int]()
        for crnt in nums {
            tranNums.append(crnt*crnt)
        }
        return tranNums.sorted()
    }
}
