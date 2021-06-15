class Solution {
func pivotIndex(_ nums: [Int]) -> Int {
    if nums.count > 1 {
        var sum = 0
        for move in nums {
            sum += move
        }
        var index = 0
        var saveNum = 0
        while index < nums.count {
            if index > 0 {
                saveNum += nums[index-1]
            }
            sum -= nums[index]
            if saveNum == sum {
                print("saveNum : \(saveNum)")
                print("sum : \(sum)")
                return index
            }
            index += 1
        }
    }
    else if nums.count == 1 {
        return 0
    }
    return -1
}
}
