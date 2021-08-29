extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func numTilePossibilities(_ tiles: String) -> Int {
        func myRecursion(_ str : String){
            var str = str
            if str == ""{
                return
            }
            visited.update(with: str)
            let strLen = str.count
            if strLen < 2{
                return
            }
            for k in 0...1{
                for _ in 0...1{
                    for i in 0...strLen {
                        var subStr = ""
                        var subStr2 = ""
                        for j in 0..<i{
                            let add = str.get(n: j)
                            subStr.insert(add, at: subStr.endIndex)
                            subStr2.insert(add, at: subStr2.startIndex)
                        }
                        if !visited.contains(subStr){
                            myRecursion(subStr)
                        }
                        if !visited.contains(subStr2){
                            myRecursion(subStr2)
                        }
                    }
                    str.insert(str.get(n: k), at: str.endIndex)
                    str.remove(at: str.index(str.startIndex, offsetBy: k))
                }
            }
        }
        var visited = Set<String>()
        myRecursion(tiles)
        return visited.count
    }
}
