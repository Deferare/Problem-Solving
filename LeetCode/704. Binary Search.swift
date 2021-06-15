class Solution {
func search(_ nums: [Int], _ target: Int) -> Int {
    var mainPot = nums.count/2
    while true {
        if mainPot > nums.count-1 || mainPot < 0 {
            break
        }
        if nums[mainPot] < target {
            mainPot += 1
            if mainPot < nums.count && nums[mainPot] > target {
                break
            }
        }
        else if nums[mainPot] > target {
            mainPot -= 1
            if mainPot >= 0 && nums[mainPot] < target {
                break
            }
        }
        else if nums[mainPot] == target {
            return mainPot
        }
        
    }
    return -1
}

}
