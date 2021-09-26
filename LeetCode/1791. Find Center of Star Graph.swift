class Solution {
    func findCenter(_ edges: [[Int]]) -> Int {
        var set = Set<Int>()
        for edge in edges{
            for node in edge{
                if set.contains(node) == true{
                    return node
                }
                else{
                    set.insert(node)
                }
            }
        }
        return 1
    }
}
