class Solution {
func maximum69Number (_ num: Int) -> Int {
    if num < 9999 {
        var str = String(num)
        for i in 0...str.count-1{
            if str.get(index: i) == "6" {
                str.remove(at: str.index(str.startIndex, offsetBy: i))
                str.insert("9", at: str.index(str.startIndex, offsetBy: i))
                break
            }
        }
        return Int(str)!
    }
    return num
}
}
extension String {
    func get(index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
