# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        mid = length // 2
        
        cur = head
        prev = None
        i = 0
        while i < mid:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            i += 1
            
        first_part = prev
        if length % 2 == 0:
            second_part = cur
        else:
            second_part = cur.next
            
        i = 0
        while i < mid:
            if first_part.val != second_part.val:
                return False
            first_part = first_part.next
            second_part = second_part.next
            i += 1
        return True
