
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def deepcopy_node(self, node, new_node, p_table):
        if not node.next:
            return

        new_node.next = Node(node.next.val)
        p_table[id(node.next)] = (new_node.next, id(node.next.random))
        
        self.deepcopy_node(node.next, new_node.next, p_table)

        new_node.next.random = p_table[ p_table[id(node.next)][1] ][0]
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        p_table = {}
        new_head = Node(head.val)
        p_table[id(None)] = (None, None)
        p_table[id(head)] = (new_head, id(head.random))
        
        self.deepcopy_node(head, new_head, p_table)
        
        new_head.random = p_table[ p_table[id(head)][1] ][0]
        return new_head
