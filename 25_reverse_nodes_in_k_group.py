# Definition for singly-linked list.
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
    def get_last_seq_node(self, node, k):
        if not node or k == 0:
            return (node, False)
        
        while k > 1 and node.next:
            node = node.next
            k -= 1
        return (node, k == 1)

    def swap_nodes(self, before_node, k, last_seq_node):
        if k < 2:
            return

        first_seq_node = before_node.next
        second_seq_node = first_seq_node.next
        after_node = last_seq_node.next
        (prev_to_last_seq_node, completed_seq) = self.get_last_seq_node(second_seq_node, k - 2)
        
        before_node.next = last_seq_node
        first_seq_node.next = after_node
        if completed_seq:
            last_seq_node.next = second_seq_node
            prev_to_last_seq_node.next = first_seq_node
            self.swap_nodes(last_seq_node, k - 2, prev_to_last_seq_node)
        else:
            last_seq_node.next = first_seq_node
    
    def reverseKGroup(self, head, k: int):
        before_node = ListNode(0, head)
        initial_node = before_node
        (last_seq_node, completed_seq) = self.get_last_seq_node(head, k)
        
        while completed_seq:
            next_before_node = before_node.next
            self.swap_nodes(before_node, k, last_seq_node)
            before_node = next_before_node
            (last_seq_node, completed_seq) = self.get_last_seq_node(before_node.next, k)
            
        return initial_node.next

s = Solution()
print( s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2) )
print( s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2) )
print( s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 3) )
print( s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 4) )
print( s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 3) )
