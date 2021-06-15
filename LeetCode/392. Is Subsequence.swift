class Solution {
func isSubsequence(_ s: String, _ t: String) -> Bool {
    var index = 0
    if s.count == 0{
        return true
    }
    if t.count == 0 || s.count > t.count{
        return false
    }
    for i in 0...t.count-1 {
        if s.get(index) == t.get(i) {
            index += 1
        }
        if index == s.count {
            return true
        }
    }
    return false
}

}

extension String {
    func get(_ index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
