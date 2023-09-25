class Solution {
    func triangleNumber(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var count = 0
        
        for i in stride(from: sortedNums.count - 1, through: 2, by: -1) {
            var start = 0
            var end = i-1
            
            while start < end {
                if sortedNums[start] + sortedNums[end] > sortedNums[i] {
                    count += end - start
                    end -= 1
                } else { start += 1 }
            }
        }
        
        return count
    }
}
