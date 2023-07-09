class Solution {
    private var preValue = Int.max
    private var minValue = Int.max
    
    func getMinimumDifference(_ root: TreeNode?) -> Int {
        guard let root = root else {return 0}
        
        self.search(root)
        
        return self.minValue
    }
    
    private func search(_ root: TreeNode?){
        guard let root = root else {return}
        
        search(root.left)
        self.minValue = min(abs(root.val - self.preValue), self.minValue)
        self.preValue = root.val
        search(root.right)
    }
}
