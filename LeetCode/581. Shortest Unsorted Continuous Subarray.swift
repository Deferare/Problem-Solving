class Solution {
func findUnsortedSubarray(_ nums: [Int]) -> Int {
    if nums.count > 1 {
        var arr = nums.sorted()
        var firstIndex = 0; var endIndex = nums.count-1
        var check = 0
        for i in 0...nums.count-1 {
            if arr[i] != nums[i] {
                firstIndex = i
                check = 1
                break
            }
        }
        if check == 1 {
            for i in (0...nums.count-1).reversed() {
                if arr[i] != nums[i] {
                    endIndex = i
                    break
                }
            }
        }
        else {
            return 0
        }
        return endIndex-firstIndex+1
    }
    return 0
}
}
