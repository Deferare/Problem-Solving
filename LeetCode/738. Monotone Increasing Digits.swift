class Solution {
    func monotoneIncreasingDigits(_ n: Int) -> Int {
        var nums: [Int] = String(n).map { Int(String($0))! }
        var firstEqual = -1
        
        func updateFirstEqual(i: Int) { if firstEqual == -1 || nums[firstEqual] < nums[i] { firstEqual = i } }
        
        for i in 0..<nums.count-1 {
            if nums[i] == nums[i+1] {
                updateFirstEqual(i: i)
            } else if nums[i] > nums[i+1] {
                updateFirstEqual(i: i)
                nums[firstEqual] -= 1
                for j in firstEqual+1..<nums.count { nums[j] = 9 }
                break
            }
        }
        
        return Int(nums.map { String($0)}.joined())!
    }
}
