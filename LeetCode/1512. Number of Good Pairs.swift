class Solution {
func numIdenticalPairs(_ nums: [Int]) -> Int {
    var arr = [Int](repeating: 0, count: 101)
    for i in 0...nums.count-1 {
        arr[nums[i]] += 1
    }    
    var result = 0
    for i in 0...arr.count-1 {
        if arr[i] != 0 && arr[i] > 1{
            var saveNum = 1
            if arr[i] == 2 {
                result += 1
            }
            else {
                for j in 2...arr[i]-1 {
                    saveNum += j
                }
                result += saveNum
            }
        }
    }
    return result
}
}
