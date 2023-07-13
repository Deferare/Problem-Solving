class Solution {
    private var memo:[Int:[TreeNode?]] = [1: [TreeNode()]]
    
    func allPossibleFBT(_ n: Int) -> [TreeNode?] {
        if n%2 == 0 {return []}
        if let memo = self.memo[n] { return memo }

        var roots = [TreeNode?]()
        
        for i in stride(from: 1, through: n - 1, by: 2){
            for left in allPossibleFBT(i){
                for right in allPossibleFBT(n - i - 1){
                    let root = TreeNode()
                    root.left = left
                    root.right = right
                    self.memo[n]?.append(root)
                    roots.append(root)
                }
            }
        }
        
        self.memo[n] = roots
        
        return roots
    }
}
