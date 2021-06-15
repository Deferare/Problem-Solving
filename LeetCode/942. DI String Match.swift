class Solution {
func diStringMatch(_ S: String) -> [Int] {
    var arr = [Int]()
    var inputI = 0; var inputD = S.count
    for i in 0...S.count-1 {
        if S.get(i) == "I" {
            arr.append(inputI)
            inputI += 1
        }
        else {
            arr.append(inputD)
            inputD -= 1
        }
    }
    arr.append(inputD)
    return arr
}
}
extension String {
    func get(_ index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
