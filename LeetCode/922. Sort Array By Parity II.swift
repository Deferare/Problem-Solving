class Solution {
    func sortArrayByParityII(_ nums: [Int]) -> [Int] {
        var evens = [Int]()
        var odds = [Int]()
        for i in 0..<nums.count{
            if i%2 == 0 && nums[i]%2 != 0{
                evens.append(i)
            }
            if i%2 != 0 && nums[i]%2 == 0{
                odds.append(i)
            }
        }
        var nums = nums
        for i in 0..<evens.count{
            let tmp = nums[evens[i]]
            nums[evens[i]] = nums[odds[i]]
            nums[odds[i]] = tmp
        }
        return nums
    }
}
