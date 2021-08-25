extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func numOfStrings(_ patterns: [String], _ word: String) -> Int {
        var sets = Set<String>()
        for idx in 0..<word.count{
            for i in 0..<word.count-idx{
                var sub_word = ""
                for j in i..<word.count-idx{
                    sub_word += String(word.get(n: j))
                }
                sets.update(with: sub_word)
            }
        }
        var result_cnt = 0
        for crnt in patterns{
            if sets.contains(crnt){
                result_cnt += 1
            }
        }
        return result_cnt
    }
}
