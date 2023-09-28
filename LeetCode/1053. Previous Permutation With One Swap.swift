class Solution {
    func prevPermOpt1(_ arr: [Int]) -> [Int] {
        var arr = arr
        var i = arr.count - 2
        while i >= 0 && arr[i] <= arr[i+1] { i -= 1 }
        
        if i >= 0 {
            var j = arr.count - 1
            while arr[j] >= arr[i] || arr[j] == arr[j-1] { j -= 1 }
            arr.swapAt(i, j)
        }
        
        return arr
    }
}
