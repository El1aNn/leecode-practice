# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
#
#         # def swap(head, pre):
#         #     tmp = pre.next
#         #     pre.next = head.next
#         #     head.next.next = tmp
#         fast, slow = head.next, head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         mid = slow.next
#         slow.next = None
#         left, right = self.sortList(head), self.sortList(mid)
#
#         def mergeTwoLists(l1, l2):
#             dummy = ListNode(0)
#             cur = dummy
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     cur.next = l1
#                     l1 = l1.next
#                 else:
#                     cur.next = l2
#                     l2 = l2.next
#                 cur = cur.next
#             cur.next = l1 if l1 else l2
#             return dummy.next
#
#         return mergeTwoLists(left, right)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        dummy = ListNode(-1)
        head = dummy
        for val in l:
            headNew = ListNode(val)
            head.next = headNew
            head = head.next
        return dummy.next
