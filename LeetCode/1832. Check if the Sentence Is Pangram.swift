class Solution {
    func checkIfPangram(_ sentence: String) -> Bool {
        var alpha_set = Set<Character>()
        for crnt in 0..<26{
            alpha_set.insert(Character(UnicodeScalar(crnt+97)!))
        }
        for crnt in sentence{
            if alpha_set.contains(crnt){
                alpha_set.remove(crnt)
            }
        }
        if alpha_set.count != 0{
            return false
        }
        return true
    }
}
