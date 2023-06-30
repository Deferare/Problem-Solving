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
    func partition(_ head: ListNode?, _ x: Int) -> ListNode? {
        let leftStart = ListNode(-1)
        let rightStart = ListNode(-1)
        
        var left = leftStart
        var right = rightStart
        var crnt = head
        while crnt != nil{
            if crnt!.val < x{
                left.next = crnt
                left = crnt!
            }else{
                right.next = crnt
                right = crnt!
            }
            crnt = crnt?.next
        }
        
        right.next = nil
        left.next = rightStart.next
        
        return leftStart.next
    }
}
