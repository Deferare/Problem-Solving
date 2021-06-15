class Solution {
func sumOddLengthSubarrays(_ arr: [Int]) -> Int {
    var sum = 0
    for i in 1...arr.count {
        if i%2 != 0 || i == 1{
            var subSum = 0
            for j in 0...arr.count-i {
                for k in j...j+i-1 {
                    subSum += arr[k]
                }
            }
            sum += subSum
        }
    }
    return sum
}
}
