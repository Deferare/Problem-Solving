class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var openBracket = 0
        var closeBracket = 0
        for crnt in s{
            if crnt == "("{
                openBracket += 1
            }
            else{
                if openBracket < 1{
                    closeBracket -= 1
                }
                else{
                    openBracket -= 1
                }
            }
        }

        return abs(openBracket)+abs(closeBracket)
    }
}
