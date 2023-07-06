class Solution {
    private var maxDepth = 0
    private var bottomCount = 0
    
    func countNodes(_ root: TreeNode?) -> Int {
        self.dfs(root, 1)
        self.maxDepth -= 1
        let sum = max(0, Int(pow(2, Float(self.maxDepth))) - 1)
        
        return sum + self.bottomCount
    }
    
    private func dfs(_ root: TreeNode?,_ depth: Int){
        if root == nil {return}
        if root?.left == nil && root?.right == nil{
            if self.maxDepth == 0{
                self.maxDepth = depth
            }
            if depth == self.maxDepth{
                self.bottomCount += 1
            }
        }
        
        dfs(root?.left, depth + 1)
        dfs(root?.right, depth + 1)
    }
}
