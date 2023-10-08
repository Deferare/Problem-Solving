class Solution {
    func twoEggDrop(_ n: Int) -> Int {
        var floor = 0, steps = 1
        
        while floor < n {
            floor += steps
            steps += 1
        }
        
        return steps-1
    }
}
