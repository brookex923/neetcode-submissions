# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next: #get mid point +1
            slow = slow.next
            fast = fast.next.next
        
        
        reversedcurr = slow
        prev = None

        while reversedcurr:
            next_node = reversedcurr.next
            reversedcurr.next = prev
            prev = reversedcurr
            reversedcurr = next_node
        
        #merge two halves together
        list1 = head
        list2 = prev
        while list2.next:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2






