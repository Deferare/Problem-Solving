class Solution {
func isValid(_ s: String) -> Bool {
    var data = [Character]()
    for i in 0...s.count-1 {
        if s.get(index: i) == "(" || s.get(index: i) == "{" || s.get(index: i) == "[" {
            data.append(s.get(index: i))
        }
        else if s.get(index: i) == ")" || s.get(index: i) == "}" || s.get(index: i) == "]" {
            if data.last == "(" && s.get(index: i) == ")"{
                data.removeLast()
            }
            else if data.last == "{" && s.get(index: i) == "}" {
                data.removeLast()
            }
            else if data.last == "[" && s.get(index: i) == "]" {
                data.removeLast()
            }
            else {
                return false
            }
        }
    }
    if data.count > 0 {
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
