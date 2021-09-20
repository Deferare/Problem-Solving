class Solution {
    func reverseWords(_ s: String) -> String {
        let arr = s.split(separator: " ")
        var result_str = ""
        for crnt in arr{
            let crnt2 = crnt.reversed()
            for i in crnt2{
                result_str += String(i)
            }
            result_str += " "
        }
        result_str.removeLast()
        return result_str
    }
}
