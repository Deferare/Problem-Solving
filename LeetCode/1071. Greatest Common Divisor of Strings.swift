class Solution {
    func gcdOfStrings(_ str1: String, _ str2: String) -> String {
        var s = Array(str1)
        var t = Array(str2)
        
        for i in stride(from: t.count-1, through: 0, by: -1){
            var gOD = t[0...i]
            
            if self.checkGOD(&s, &gOD) && self.checkGOD(&t, &gOD){
                return String(gOD)
            }
        }
        
        return ""
    }
    
    private func checkGOD(_ s: inout [Character],_ t: inout Array<Character>.SubSequence) -> Bool{
        if s.count%t.count != 0 { return false }
        
        for j in 0..<s.count{
            if s[j] != t[j%(t.count)]{
                return false
            }
        }
        
        return true
    }
}
