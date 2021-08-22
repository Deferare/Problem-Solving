class Solution {
    func freqAlphabets(_ s: String) -> String {
        var result_str = ""
        var index = 0
        while index < s.count {
            if index+2 < s.count && s[s.index(s.startIndex, offsetBy: index+2)] == "#"{
                result_str += String(UnicodeScalar(Int(String(s[s.index(s.startIndex, offsetBy: index)])+String(s[s.index(s.startIndex, offsetBy: index+1)]))!+96)!)
                index += 2
            }
            else{
                result_str += String(UnicodeScalar(Int(String(s[s.index(s.startIndex, offsetBy: index)]))!+96)!)
            }
            index += 1
        }
        return result_str
    }
}
