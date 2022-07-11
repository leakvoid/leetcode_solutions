class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        dummy = ListNode(0, head)
        
        cur = dummy
        pos = 0
        while pos < left - 1:
            cur = cur.next
            pos += 1
        before_node = cur
        first_node = cur.next
        
        prev = before_node
        cur = first_node
        for pos in range(left, right + 1):
            n = cur.next
            cur.next = prev
            prev, cur = cur, n
        
        first_node.next = cur
        before_node.next = prev
        return dummy.next
