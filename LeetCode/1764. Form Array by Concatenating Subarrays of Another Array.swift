class Solution {
    func canChoose(_ groups: [[Int]], _ nums: [Int]) -> Bool {
        var count = 0
        var left = 0
        
        for i in 0..<groups.count {
            var right = left + groups[i].count-1
            while right < nums.count {
                if nums[left] == groups[i][0] && nums[right] == groups[i][groups[i].count-1] {
                    var check = true
                    
                    for j in 0..<groups[i].count-1 {
                        if groups[i][j] == nums[left] { left += 1 }
                        else {
                            check = false
                            break
                        }
                    }
                    
                    left += 1
                    right = left + groups[i].count-1
                    
                    if check {
                        count += 1
                        break
                    }
                } else {
                    left += 1
                    right += 1
                }
            }
        }
        
        return count == groups.count
    }
}
