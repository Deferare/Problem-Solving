/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        if head == nil {return head}
        
        var answer:ListNode?
        var left:ListNode?
        var pre = left
        var crnt = head
        while crnt != nil{
            if crnt?.val != pre?.val && crnt?.val != crnt?.next?.val{
                left?.next = crnt
                left = crnt!
                if answer == nil{
                    answer = left
                }
            }else{
                left?.next = nil
            }
            pre = crnt!
            crnt = crnt?.next
        }
        
        return answer
    }
}
