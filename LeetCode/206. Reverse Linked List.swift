class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var previousNode:ListNode? = nil
        var currentNode = head
        while currentNode != nil{
            let nextNode = currentNode?.next
            currentNode?.next = previousNode
            previousNode = currentNode!
            currentNode = nextNode
        }
        return previousNode
    }
}
