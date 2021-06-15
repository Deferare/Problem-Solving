class Solution {
func selfDividingNumbers(_ left: Int, _ right: Int) -> [Int] {
    var arr = [Int]()
    for num in left...right {
        let str = String(num)
        var check = 0
        for i in 0...str.count-1 {
            if Int(String(str.get(index: i))) == 0 {
                check = 1
                break
            }
            if num%Int(String(str.get(index: i)))! != 0 {
                check = 1
                break
            }
        }
        if check == 0 {
            arr.append(num)
        }
    }
    return arr
}
}
extension String {
    func get(index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
