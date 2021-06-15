class Solution {
func canPartition(_ nums: [Int]) -> Bool {
    var sum : Int {
        var s = 0
        for move in nums {
            s += move
        }
        if s%2 != 0 {
            return -1
        }
        return s/2
    }
    if sum != -1 {
        var memo = [Int](repeating: -1, count: sum+1)
        func dp(_ nums:[Int],_ amount:Int) -> Bool {
            if amount < 0 {
                return false
            }
            if memo[amount] == 1 {
                return true
            }
            else if memo[amount] == 0{
                return false
            }
            if nums.count == 1 {
                if nums[0] == amount {
                    memo[amount] = 1
                    return true
                }
                else {
                    return false
                }
            }
            let amount = amount
            let saveN = nums[nums.count-1]
            let arr = [Int](nums[0...nums.count-2])
            let r1 = dp(arr, amount-saveN)
            if r1 == true {
                memo[amount] = 1
                return true
            }
            let r2 = dp(arr, amount)
            var subRe = false
            if r1 || r2 {
                memo[amount] = 1
                subRe = true
            }
            else if subRe == false {
                memo[amount] = 0
            }
            return subRe
        }
        let result = dp(nums, sum)
        return result
    }
    return false
}
}
