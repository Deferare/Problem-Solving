class Solution {
    func countKDifference(_ nums: [Int], _ k: Int) -> Int {
        var resultCnt = 0
        for i in 0..<nums.count-1{
            for j in i+1..<nums.count{
                if abs(nums[i]-nums[j]) == k{
                    resultCnt += 1
                }
            }
        }
        return resultCnt
    }
}
