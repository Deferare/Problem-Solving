class Solution {
    var maxSum = Int.min
    
    func maxPathSum(_ root: TreeNode?) -> Int {
        let _ = self.dfs(root)
        
        return self.maxSum
    }
    
    private func dfs(_ root: TreeNode?) -> Int{
        guard let root = root else {return 0}
        
        let leftGain = max(dfs(root.left), 0)
        let rightGain = max(dfs(root.right), 0)
        let totalGain = leftGain + rightGain + root.val
        
        self.maxSum = max(self.maxSum, totalGain)
        
        return max(leftGain, rightGain) + root.val
    }
}
