class Solution {
func climbStairs(_ n: Int) -> Int {
    var arr = [Int](repeating: 0, count: n+1)
    arr[0] = 1
    arr[1] = 2
    if n > 2 {
        let result = 0
        for i in 2...n-1 {
            arr[i] = arr[i-1] + arr[i-2]
        }
    }
    return arr[n-1]
}
}
