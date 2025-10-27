# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


            s = Solution()
            ln = ListNode()
            ln2 = ListNode()

            for i in range(3):
                ln.val = i + 1
                if i != 0:
                    ln.next



s = Solution()
s.mergeTwoLists([1,2,4], [1,3,4])