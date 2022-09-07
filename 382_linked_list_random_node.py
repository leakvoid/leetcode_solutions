import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.ll_len = 0
        
        node = self.head
        while node:
            self.ll_len += 1
            node = node.next

    def getRandom(self) -> int:
        node_i = random.randint(0, self.ll_len - 1)
        node = self.head
        while node_i > 0:
            node = node.next
            node_i -= 1
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
