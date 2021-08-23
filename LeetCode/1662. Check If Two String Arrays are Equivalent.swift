extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func arrayStringsAreEqual(_ word1: [String], _ word2: [String]) -> Bool {
        var save_str_1 = ""
        var save_str_2 = ""
        for crnt in word1{
            save_str_1 += crnt
        }
        for crnt in word2{
            save_str_2 += crnt
        }
        if save_str_1.count != save_str_2.count{
            return false
        }
        else{
            for i in 0..<save_str_1.count{
                if save_str_1.get(n: i) != save_str_2.get(n: i){
                    return false
                }
            }
        }
        return true
    }
}
