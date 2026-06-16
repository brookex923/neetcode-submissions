# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev # changes point direction
            prev = curr #shift prev
            curr = temp #shift curr
        return prev