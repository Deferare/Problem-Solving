class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        let nums = nums.sorted()
        var closest = nums[0] + nums[1] + nums[2]
        
        for i in 0..<nums.count{
            var left = i + 1
            var right = nums.count - 1
            
            while left < right{
                let sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(target - closest){ closest = sum }
                if sum == target {return sum}
                else if sum < target{
                    left += 1
                }else{
                    right -= 1
                }
            }
        }
        
        return closest
    }
}
