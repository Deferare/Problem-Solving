extension String{
    subscript(i:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: i)]
    }
}

class Solution {
    func removeDuplicateLetters(_ s: String) -> String {
        let lenth = s.count
        var count = Dictionary<Character, Int>()
        
        for i in 0..<lenth{
            if count[s[i]] == nil{
                count[s[i]] = 1
            }else{
                count[s[i]]! += 1
            }
        }

        var answer = Array<Character>()
        var cache = Set<Character>()
        
        for i in 0..<lenth{
            count[s[i]]! -= 1
            if cache.contains(s[i]){
                continue
            }
            
            while !answer.isEmpty && count[answer.last!]! > 0 && answer.last! > s[i]{
                let pop = answer.popLast()
                cache.remove(pop!)
            }
            
            answer.append(s[i])
            cache.insert(s[i])
        }
        
        var result = ""
        for i in 0..<answer.count{
            result += answer[i].description
        }
        
        return result
    }
}
