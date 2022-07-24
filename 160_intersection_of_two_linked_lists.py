# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_pointers = set()
        
        node_a = headA
        while node_a:
            a_pointers.add(id(node_a))
            node_a = node_a.next
            
        node_b = headB
        while node_b:
            if id(node_b) in a_pointers:
                return node_b
            node_b = node_b.next
            
        return None
