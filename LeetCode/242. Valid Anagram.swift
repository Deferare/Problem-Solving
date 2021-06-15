class Solution {
func isAnagram(_ s: String, _ t: String) -> Bool {
    var dic = [Character:Int]()
    if s.count == t.count {
        for move in s {
            dic[move] = (dic[move] ?? 0) + 1
        }

        for move in t {
            if dic[move] == 0 {
                return false
            }
            else {
                dic[move] = (dic[move] ?? 0) - 1
                if dic[move] == -1 {return false}
            }
        }

    }
    else {
        return false
    }
    return true
}
}
