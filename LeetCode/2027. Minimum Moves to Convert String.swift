class Solution {
    func minimumMoves(_ s: String) -> Int {
        var arr = [Character]()
        for crnt in s{
            arr.append(crnt)
        }
        var result = 0
        for i in 0..<s.count-2{
            if arr[i] == "X"{
                arr[i+1] = "O"
                arr[i+2] = "O"
                result += 1
            }
        }
        if arr[arr.count-2] == "X" || arr[arr.count-1] == "X"{
            result += 1
        }
        return result
    }
}
