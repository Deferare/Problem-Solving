class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var resultIndex = -1
        for i in 0..<nums.count{
            if nums[i] >= target{
                resultIndex = i
                break
            }
            else{
                resultIndex = i+1
            }
        }
        return resultIndex
    }
}
