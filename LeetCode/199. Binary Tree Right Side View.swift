class Solution {
    private var answer = [Int]()
    
    func rightSideView(_ root: TreeNode?) -> [Int] {
        self.dfs(root, 1)
        
        return self.answer
    }
    
    private func dfs(_ root:TreeNode?,_ depth:Int){
        guard let root = root else {return}
        
        if depth > self.answer.count{
            self.answer.append(root.val)
        }
        
        dfs(root.right, depth + 1)
        dfs(root.left, depth + 1)
    }
}
