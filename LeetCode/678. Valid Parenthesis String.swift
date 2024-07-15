class Solution {
    private func checker(_ s: String, _ open: Character, _ close: Character) -> Bool {
        var balance = 0
        var star = 0
        
        for char in s {
            if char == open {
                balance += 1
            } else if char == close {
                if balance > 0 {
                    balance -= 1
                } else if star > 0{
                    star -= 1
                } else {
                    return false
                }
            } else {
                star += 1
            }
        }
        
        return balance <= star
    }
    
    func checkValidString(_ s: String) -> Bool {
        return checker(s, "(", ")") && checker(String(s.reversed()), ")", "(")
    }
}
