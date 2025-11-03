# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        headA = ListNode()
        tailA = headA

        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                tailA.next = list1
                list1 = list1.next
                tailA = tailA.next
            else:
                tailA.next = list2
                list2 = list2.next
                tailA = tailA.next

        tailA.next = list2 if list1 is None else list1

        return headA

s = Solution()

l1 = ListNode()
l2 = ListNode()



s.mergeTwoLists(l1, l2)