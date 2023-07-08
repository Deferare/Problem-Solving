class Solution {
    func averageOfLevels(_ root: TreeNode?) -> [Double] {
        var answer = [Double]()
        var q = [TreeNode?]()
        
        if let root = root{
            q.append(root)
        }
        
        while q.count > 0{
            var avg:Double = 0
            let count = q.count
            
            for _ in 0..<count{
                let pop = q.removeFirst()
                
                if let pop = pop{
                    if pop.left != nil {q.append(pop.left)}
                    if pop.right != nil {q.append(pop.right)}
                    
                    avg += Double(pop.val)
                }
            }
            
            answer.append(avg/Double(count))
        }
        
        return answer
    }
}
