class Solution {
    func sumNumbers(_ root: TreeNode?) -> Int {
        return dfs(root, 0)
    }
    
    func dfs(_ node: TreeNode?, _ val: Int) -> Int {
        guard let node = node else {
            return 0
        }

        let totalVal = val * 10 + node.val

        if node.left == nil && node.right == nil {
            return totalVal
        }
        
        return dfs(node.left, totalVal) + dfs(node.right, totalVal)
    }
}
