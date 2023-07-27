class Solution {
    func mctFromLeafValues(_ arr: [Int]) -> Int {
        var stack = [Int]()
        var sum = 0

        for num in arr{
            while let last = stack.last, last <= num{
                stack.removeLast()
                sum += last * min(stack.last ?? Int.max, num)
            }
            stack.append(num)
        }
        
        while stack.count > 1{
            sum += stack.removeLast() * stack.last!
        }
        
        return sum
    }
}
