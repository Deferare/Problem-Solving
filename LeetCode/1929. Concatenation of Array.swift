class Solution {
    func getConcatenation(_ nums: [Int]) -> [Int] {
        var result = nums
        for crnt in nums {
            result.append(crnt)
        }
        return result
    }
}
