# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        last_sorted_node = head
        removed_node = head.next
        while removed_node:
            if removed_node.val >= last_sorted_node.val:
                last_sorted_node = removed_node
                removed_node = last_sorted_node.next
                continue
            
            last_sorted_node.next = removed_node.next
            
            prev_sorted_node = dummy
            sorted_node = dummy.next
            while sorted_node != last_sorted_node.next:
                if removed_node.val < sorted_node.val:
                    prev_sorted_node.next = removed_node
                    removed_node.next = sorted_node
                    break
                prev_sorted_node = sorted_node
                sorted_node = sorted_node.next
            
            removed_node = last_sorted_node.next        
        
        return dummy.next
