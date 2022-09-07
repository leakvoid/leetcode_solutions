# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd = ListNode()
        dummy_even = ListNode()
        last_odd = dummy_odd
        last_even = dummy_even
        
        node = head
        idx = 0
        while node:
            if idx % 2:
                last_odd.next = node
                last_odd = last_odd.next
            else:
                last_even.next = node
                last_even = last_even.next
            node = node.next
            idx += 1
        
        last_odd.next = None
        last_even.next = dummy_odd.next
        return dummy_even.next
