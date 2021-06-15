class Solution {
func dailyTemperatures(_ T: [Int]) -> [Int] {
    let arr = T
    var data = Array<Int>()
    var result = Array<Int>()
    for i in (0...arr.count-1).reversed() {
        if arr[i] >= arr[data.last ?? i] {
            while arr[i] >= arr[data.last ?? i] {
                if data.count != 0 {data.removeLast()}
                else {
                    break
                }
            }
            result.append((data.last ?? i) - i)
            data.append(i)
        }
        else {
            result.append((data.last ?? i) - i)
            data.append(i)
        }
    }
    result.reverse()
    return result
}
}
