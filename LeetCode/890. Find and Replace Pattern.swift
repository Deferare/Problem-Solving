extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func findAndReplacePattern(_ words: [String], _ pattern: String) -> [String] {
    var dict = Dictionary<Character, Int>()
    var indexSave = [Array<Any>]()
    for i in 0..<pattern.count{
        if dict[pattern.get(n: i)] != nil{
            indexSave[dict[pattern.get(n: i)]!].append(i)
        }
        else{
            indexSave.append([i])
            dict[pattern.get(n: i)] = indexSave.count-1
        }
    }
    var resultStr = [String]()
    for word in words{
        var visited = Set<Character>()
        var check = 0
        for indexs in indexSave{
            if visited.contains(word.get(n: indexs[0] as! Int)) == false{
                visited.update(with: word.get(n: indexs[0] as! Int))
            }else{
                check = 1
                break
            }
            
            for i in 1..<indexs.count{
                if word.get(n: indexs[0] as! Int) != word.get(n: indexs[i] as! Int){
                    check = 1
                    break
                }
            }
        }
        if check == 0{
            resultStr.append(word)
        }
    }
    return resultStr
}
}
