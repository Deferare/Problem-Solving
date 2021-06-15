class Solution {
func minOperations(_ boxes: String) -> [Int] {
    var dic = [String:Int]()
    var dicKey = [String]()
    for i in 0...boxes.count-1 {
        if boxes.get(i) == "1" {
            dic[String(i)] = i
            dicKey.append(String(i))
        }
    }
    var result = [Int]()
    if dicKey.count > 0 {
        for i in 0...boxes.count-1 {
            var put = 0
            for j in 0...dicKey.count-1 {
                var save = dic[dicKey[j]]! - i
                if save < 0 {
                    save *= -1
                }
                put += save
            }
            result.append(put)
        }
    }
    else {
        result = [Int](repeating: 0, count: boxes.count)
    }
    return result
}

}

extension String {
    func get(_ index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
