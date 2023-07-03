class Solution {
    func reverseKGroup(_ head: ListNode?, _ k: Int) -> ListNode? {
        let answer = ListNode(-1, head)
        var pre:ListNode? = answer
        var end:ListNode? = answer
        
        while end?.next != nil{
            for _ in 0..<k{
                end = end?.next
            }
            
            if end == nil {break}
            
            let start = pre?.next
            let next = end?.next

            end?.next = nil
            pre?.next = self.reverse(start)
            start?.next = next
            
            pre = start
            end = pre
        }
        
        return answer.next
    }
    
    func reverse(_ head: ListNode?) -> ListNode?{
        var pre: ListNode? = nil
        var crnt = head
        while crnt != nil {
            let next = crnt?.next
            crnt?.next = pre
            pre = crnt
            crnt = next
        }
        return pre
    }
}
