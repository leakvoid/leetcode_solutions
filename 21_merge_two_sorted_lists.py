class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        list3 = head
        
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
            
        if list1:
            list3.next = list1
        
        if list2:
            list3.next = list2
            
        return head

    # copy nodes instead of merge
    def createMergedList(self, list1, list2):
        if list1.val < list2.val:
            val = list1.val
            list1 = list1.next
        else:
            val = list2.val
            list2 = list2.next
        head = ListNode(val)
        list3 = head
        
        while list1 and list2:
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            
            list3.next = ListNode(val)
            list3 = list3.next
            
        while list1:
            list3.next = ListNode(list1.val)
            list3 = list3.next
            list1 = list1.next
        
        while list2:
            list3.next = ListNode(list2.val)
            list3 = list3.next
            list2 = list2.next
            
        return head
