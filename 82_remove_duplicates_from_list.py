# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        
        prev = head
        cur = prev.next
        last_unique = None
        deletion_flag = False
        
        while cur:
            if prev.val == cur.val:
                deletion_flag = True
            elif deletion_flag:
                deletion_flag = False
                if last_unique:
                    last_unique.next = cur
                else:
                    head = cur
            else:
                last_unique = prev
            prev, cur = cur, cur.next
            
        if deletion_flag:
            if last_unique:
                last_unique.next = cur
            else:
                head = cur
        
        return head

s = Solution()
print(s.deleteDuplicates( ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))) ))
print(s.deleteDuplicates( ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))) ))
print(s.deleteDuplicates( ListNode(1, ListNode(1, ListNode(1))) ))
