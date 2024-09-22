# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p.next != None and p != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return dummy.next


S = Solution()
print(S.removeElements([1, 2, 3, 4, 5, 6], 5))
