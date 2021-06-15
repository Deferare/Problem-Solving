class Solution {
func wordPattern(_ pattern: String, _ s: String) -> Bool {
    var str = [String]()
    var saveStr = ""
    for i in 0...s.count-1 {
        if s.get(index: i) != " "{
            saveStr.append(s.get(index: i))
        }
        if i == s.count-1 || s.get(index: i) == " "{
            str.append(saveStr)
            saveStr = ""
        }
    }
    if pattern.count == str.count {
        var dic = [Character:String]()
        for i in 0...pattern.count-1 {
            if dic[pattern.get(index: i)] == nil {
                if dic.count >= 1 {
                    for j in 0...i-1 {
                        if dic[pattern.get(index: j)] == String(str[i]) {
                            return false
                        }
                    }
                }
                dic[pattern.get(index: i)] = String(str[i])
            }
            else if dic[pattern.get(index: i)]! != String(str[i]) {
                return false
            }
        }
    }
    else {
        return false
    }
    return true
}
}
extension String {
    func get(index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
