class Solution {
    func summaryRanges(_ nums: [Int]) -> [String] {
        let length = nums.count
        var answer = [String]()
        var start = 0
        var end = 0
        while end < length{
            end += 1
            if end == length || nums[end - 1] + 1 != nums[end]{
                if nums[start] != nums[end - 1]{
                    answer.append("\(nums[start])->\(nums[end - 1])")
                }else{
                    answer.append("\(nums[start])")
                }
                start = end
            }
        }
        return answer
    }
}
