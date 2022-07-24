# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        p_table = set()
        p_table.add(id(head))
        
        node = head
        while node.next:
            if id(node.next) in p_table:
                return True
            p_table.add(id(node.next))
            node = node.next
            
        return False
