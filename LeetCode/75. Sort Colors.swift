class Solution {
func sortColors(_ nums: inout [Int]) {
    var red = 0
    var green = 0
    var blue = 0
    for i in 0...nums.count-1 {
        if nums[i] == 0 {
            red += 1
        }
        else if nums[i] == 1 {
            green += 1
        }
        else if nums[i] == 2 {
            blue += 1
        }
    }
    var index = 0
    while red != 0 {
        nums[index] = 0
        red -= 1
        index += 1
    }
    while green != 0 {
        nums[index] = 1
        green -= 1
        index += 1
    }
    while blue != 0 {
        nums[index] = 2
        blue -= 1
        index += 1
    }
}
}
