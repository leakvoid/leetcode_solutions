# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p_table = {}
        p_table[id(head)] = head
        
        node = head
        while node.next:
            if id(node.next) in p_table:
                return p_table[id(node.next)]

            p_table[id(node.next)] = node.next
            node = node.next
            
        return None
