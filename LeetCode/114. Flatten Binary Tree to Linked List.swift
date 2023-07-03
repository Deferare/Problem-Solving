class Solution {
    var crnt:TreeNode? = nil
    
    func flatten(_ root: TreeNode?) {
        if root == nil {return}
        
        self.crnt = root
        
        let left = root?.left
        let right = root?.right
        
        root?.right = left
        
        flatten(left)
        
        self.crnt?.right = right
        
        flatten(right)
        
        root?.left = nil
    }
}
