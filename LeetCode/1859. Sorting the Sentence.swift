class Solution {
    func sortSentence(_ s: String) -> String {
        var s_arr = Array(s.split(separator: " "))
        s_arr.sort {$0[$0.index($0.startIndex, offsetBy: $0.count-1)] < $1[$1.index($1.startIndex, offsetBy: $1.count-1)]}
        var result_str = ""
        for i in 0...s_arr.count-1{
            for j in 0...s_arr[i].count-2{
                result_str += String(s_arr[i][s_arr[i].index(s_arr[i].startIndex, offsetBy: j)])
            }
            if i != s_arr.count-1{
                result_str += " "
            }
        }
        return result_str
    }
}
