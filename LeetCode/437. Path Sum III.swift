/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> Int {
        var count = 0
        var prefixSum: Dictionary<Int, Int> = [:]
        prefixSum[0] = 1
        
        func dfs(_ node: TreeNode?,_ currentSum: Int) {
            guard let node = node else { return }
            
            let newSum = currentSum + node.val
            
            if let preCount = prefixSum[newSum - targetSum] {
                count += preCount
            }
            
            prefixSum[newSum, default: 0] += 1
            
            dfs(node.left, newSum)
            dfs(node.right, newSum)
            
            prefixSum[newSum]! -= 1
        }
        
        dfs(root, 0)
        
        return count
    }
}
