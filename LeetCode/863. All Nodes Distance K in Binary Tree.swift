class Solution {
    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        func searchDown(_ crnt:TreeNode?,_ bias:Int){
            guard let crnt = crnt else {return}
            if bias > k {return}
            if bias == k {answer.append(crnt.val)}
            else{
                searchDown(crnt.left, bias + 1)
                searchDown(crnt.right, bias + 1)
            }
        }
        
        func searchUp(_ crnt:TreeNode?) -> Int?{
            guard let crnt = crnt else {return nil}
            if crnt.val == target?.val{
                searchDown(target, 0)
                return 1
            }
            
            let left = searchUp(crnt.left)
            let right = searchUp(crnt.right)
            
            if left == k || right == k{
                answer.append(crnt.val)
            }else if left ?? -1 > k || right ?? -1 > k{
                return nil
            }else{
                if let left = left{
                    searchDown(crnt.right, left + 1)
                    return left + 1
                }
                if let right = right{
                    searchDown(crnt.left, right + 1)
                    return right + 1
                }
            }
            
            return nil
        }
        
        var answer = [Int]()
        let _ = searchUp(root)
        
        return answer
    }
}
