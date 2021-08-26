class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        var set = Set<Character>()
        for crnt in allowed{
            set.update(with: crnt)
        }
        var result_cnt = 0
        for crnt in words{
            var check = 0
            for crnt in crnt{
                if !set.contains(crnt){
                    check = 1
                    break
                }
            }
            if check == 0{
                result_cnt += 1
            }
        }
        return result_cnt
    }
}
