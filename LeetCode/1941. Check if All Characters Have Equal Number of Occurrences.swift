extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func areOccurrencesEqual(_ s: String) -> Bool {
        var checkDick = Dictionary<Character,Int>()
        for crnt in s{
            if checkDick[crnt] == nil{
                checkDick[crnt] = 1
            }
            else{
                checkDick[crnt]! += 1
            }
        }
        var pre_key = checkDick[s.get(n: 0)]
        for value in checkDick.values{
            if value != pre_key{
                return false
            }
            pre_key = value
        }
        return true
    }
}
