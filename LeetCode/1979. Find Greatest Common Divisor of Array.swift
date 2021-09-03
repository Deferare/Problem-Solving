class Solution {
    func findGCD(_ nums: [Int]) -> Int {
        var minNumber = nums[0]
        var maxNumber = nums[0]
        for crnt in nums{
            if crnt > maxNumber{
                maxNumber = crnt
            }
            if crnt < minNumber{
                minNumber = crnt
            }
        }
        var result = minNumber-(maxNumber%minNumber)
        if minNumber%result != 0 || maxNumber%result != 0{
            while true{
                if minNumber%result == 0 && maxNumber%result == 0{
                    break
                }
                else{
                    result -= 1
                }
            }
        }
        return result
    }
}
