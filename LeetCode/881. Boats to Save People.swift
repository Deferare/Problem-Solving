class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        let people = people.sorted()
        var boats = 0
        var left = 0, right = people.count - 1
        
        while left <= right {
            if people[left] + people[right] <= limit {
                left += 1
            }
            
            right -= 1
            boats += 1
        }
        
        return boats
    }
}
