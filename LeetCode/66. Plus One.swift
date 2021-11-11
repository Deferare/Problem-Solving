class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var digits = digits
        var state = 1
        for i in (0..<digits.count).reversed(){
            if state == 1{
                digits[i] += 1
                if digits[i] > 9{
                    digits[i] = 0
                }
                else{
                    state = 0
                }
            }else{
                break
            }
        }
        if state == 1{
            digits.insert(1, at: 0)
        }
        return digits
    }
}
