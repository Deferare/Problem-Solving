class Solution {
func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
    var result = [Bool](repeating: false, count: candies.count)    
    for i in 0...candies.count-1 {
        if candies[i]+extraCandies >= candies.max()! {
            result[i] = true
        }
    }
    return result
}
}
