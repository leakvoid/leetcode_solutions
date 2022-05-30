class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        s = "[" + str(self.val)
        cur = self
        while cur.next:
            cur = cur.next
            s += "," + str(cur.val)
        s += "]"
        return s

class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        cur = head
        sz = 1
        while cur.next:
            cur = cur.next
            sz += 1
        
        steps = sz - n - 1
        if steps < 0:
            return head.next
        
        prior_node = head
        for i in range(0, steps):
            prior_node = prior_node.next
        deleted_node = prior_node.next
        prior_node.next = deleted_node.next
        
        return head

s = Solution()
print(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2))
print(s.removeNthFromEnd(ListNode(1,ListNode(2)),1))
print(s.removeNthFromEnd(ListNode(1),1))
print(s.removeNthFromEnd(ListNode(1,ListNode(2)),2))
