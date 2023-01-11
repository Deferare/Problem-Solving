class Solution {
    func partitionString(_ s: String) -> Int {
        let str:Array<Character> = s.map({char in char})
        let lenth = str.count
        var answer = 1
        var ceche = Set<Character>()
        for i in 0..<lenth{
            if ceche.contains(str[i]){
                answer += 1
                ceche.removeAll()
                ceche.insert(str[i])
            }else{
                ceche.insert(str[i])
            }
        }
        return answer
    }
}
