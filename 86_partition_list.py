class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        if not head:
            return None
        
        dummy = ListNode(-1000, head)
        
        if head.val < x:
            last_small = head
            first_large = None
        else:
            last_small = dummy
            first_large = head
        
        prev = head
        cur = prev.next
        while cur:
            if cur.val < x and prev.val >= x:
                prev.next = cur.next
                
                last_small.next = cur
                last_small = cur
                cur.next = first_large
                
                cur = prev.next
                continue
            elif cur.val < x and prev.val < x:
                last_small = cur
            elif not first_large:
                first_large = cur
            prev, cur = cur, cur.next
                
        return dummy.next

s = Solution()
print( s.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 1) )
