class Solution {
func sumOfUnique(_ nums: [Int]) -> Int {
    var arr = [Int](repeating: 0, count: 101)
    for i in 0...nums.count-1 {
        arr[nums[i]] += 1
    }
    var sum = 0
    for i in 0...arr.count-1 {
        if arr[i] == 1 {
            sum += i
        }
    }
    return sum
}
}
