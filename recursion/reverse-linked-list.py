class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or last node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Reverse the pointer of the next node to point back to current
        head.next.next = head
        head.next = None
        
        return new_head