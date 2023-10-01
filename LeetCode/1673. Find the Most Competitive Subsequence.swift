class Solution {
    func mostCompetitive(_ nums: [Int], _ k: Int) -> [Int] {
        var stack: [Int] = []
        var elementsLeft = nums.count
        
        for num in nums {
            while let last = stack.last, last > num, k - stack.count < elementsLeft { stack.removeLast() }
            if stack.count < k { stack.append(num) }
            elementsLeft -= 1
        }
        
        return stack
    }
}
