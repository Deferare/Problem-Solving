class Solution {
func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
    let arr = nums.sorted(by: >)
    var dic = [String:Int]()
    for i in 0...arr.count-1 {
        if dic[String(arr[i])] == nil {
            dic[String(arr[i])] = i+1
        }
        else {
            dic[String(arr[i])] = dic[String(arr[i])]! + 1
        }
    }
    var result = [Int](repeating: -1, count: nums.count)
    for i in 0...arr.count-1 {
        result[i] = nums.count - dic[String(nums[i])]!
    }
    return result
}
}
