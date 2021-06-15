class Solution {
func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
    var arr = matrix
    var memo = [Array](repeating: [Int](repeating: -1, count: 302), count: 302)
    var check = false
    func dp(arr : [[Int]], i:Int, j:Int){
        if check == false {
            if arr[i][j] == target {
                check = true
                return
            }
            if memo[i][j] == -1 {
                if i != arr.count-1 && j != arr[i].count-1 && arr[i][j] <= arr[i+1][j+1] && memo[i+1][j+1] == -1 {
                    dp(arr: arr, i: i+1, j: i+1)
                }
                if i != arr.count-1 && arr[i][j] <= arr[i+1][j] && memo[i+1][j] == -1{
                    dp(arr: arr, i: i+1, j: j)
                }
                if j != arr[i].count-1 && arr[i][j] <= arr[i][j+1] && memo[i][j+1] == -1 {
                    dp(arr: arr, i: i, j: j+1)
                }
                memo[i][j] = arr[i][j]
            }
        }
    }
    dp(arr: arr, i: 0, j: 0)
    return check
}
}
