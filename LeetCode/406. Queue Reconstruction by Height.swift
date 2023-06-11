class Solution {
    func reconstructQueue(_ people: [[Int]]) -> [[Int]] {
        let sortedPeople = people.sorted{
            if $0[0] == $1[0]{
                return $0[1] < $1[1]
            }
            return $0[0] > $1[0]
        }
        var result = [[Int]]()
        for person in sortedPeople {
            result.insert(person, at: person[1])
        }
        return result
    }
}
