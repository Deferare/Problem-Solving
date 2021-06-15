class Solution {
func busyStudent(_ startTime: [Int], _ endTime: [Int], _ queryTime: Int) -> Int {
    var num = 0
    for i in 0...startTime.count-1 {
        if startTime[i] <= queryTime && endTime[i] >= queryTime {
            num += 1
        }
    }
    return num
}
}
