# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and append the smaller value to current
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If either list is not empty, append the remaining elements
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list is next to the dummy node
        return dummy.next