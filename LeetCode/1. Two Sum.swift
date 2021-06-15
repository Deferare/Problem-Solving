class Solution {
func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var arr = nums.sorted()
    var firstIndex = 0; var endIndex = arr.count-1
    while true {
        var value = arr[firstIndex] + arr[endIndex]
        if value == target {
            break
        }
        else {
            if value < target {
                firstIndex += 1
            }
            else if value > target {
                endIndex -= 1
            }
        }
    }
    return [nums.firstIndex(of: arr[firstIndex])!, nums.lastIndex(of: arr[endIndex])!]
}
}
