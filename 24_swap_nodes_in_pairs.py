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
    def swapPairs(self, head):
        if not head.next:
            return head
       
        prev = head
        head = head.next
        prev.next = head.next
        head.next = prev
        #print("head -> next", head.val, head.next.val, "prev -> next", prev.val, prev.next.val)
   
        while prev.next:
            first = prev.next
            second = first.next
            #print("first:", first.val, "second:", second.val)
            if not second:
                break
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            #print("swapped first -> next", second.val, second.next.val, "second -> next", first.val, first.next)

        return head

s = Solution()
print(s.swapPairs(ListNode(1,ListNode(2,ListNode(3,ListNode(4))))))
