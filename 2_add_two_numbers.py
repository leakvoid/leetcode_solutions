# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        reminder = 0
        c_val = l1.val + l2.val + reminder
        if c_val >= 10:
            c_val -= 10
            reminder = 1
        else:
            reminder = 0
        
        res_head = ListNode(c_val)
        prev_node = res_head
        
        while l1.next or l2.next or reminder == 1:
            if l1.next:
                l1 = l1.next
                l1_val = l1.val
            else:
                l1_val = 0
                
            if l2.next:
                l2 = l2.next
                l2_val = l2.val
            else:
                l2_val = 0
                
            c_val = l1_val + l2_val + reminder
            if c_val >= 10:
                c_val -= 10
                reminder = 1
            else:
                reminder = 0
        
            next_node = ListNode(c_val)
            prev_node.next = next_node
            prev_node = next_node
            
        return res_head

s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
l_res = s.addTwoNumbers(l1, l2)
res = []
while l_res:
    res.append(l_res.val)
    l_res = l_res.next
print(res)
