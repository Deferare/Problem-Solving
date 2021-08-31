class Solution {
    func repeatedNTimes(_ nums: [Int]) -> Int {
        let numsLen = nums.count
        var cntDict = Dictionary<Int,Int>()
        for crnt in nums{
            if (cntDict[crnt] != nil){
                cntDict[crnt]! += 1
            }
            else{
                cntDict[crnt] = 1
            }
            if (cntDict[crnt] != nil) {
                if (cntDict[crnt]! >= Int(numsLen/2)){
                    return crnt
                }
            }
        }
        return nums[0]
    }
}
