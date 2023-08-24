class Solution {
    func maximizeGreatness(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var count = 0
        
        for num in nums {
            if num > nums[count] {
                count += 1
            }
        }
        
        return count
    }
}
