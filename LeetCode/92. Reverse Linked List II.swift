class Solution {
    func reverseBetween(_ head: ListNode?, _ left: Int, _ right: Int) -> ListNode? {
        let dummyNode = ListNode(-1, head)
        var preNode = dummyNode
        
        for _ in 0..<left-1{
            preNode = preNode.next!
        }
        
        let crntNode = preNode.next
        for _ in 0..<right-left{
            let next = crntNode?.next
            crntNode?.next = next?.next
            next?.next = preNode.next
            preNode.next = next
        }
        
        return dummyNode.next
    }
}
