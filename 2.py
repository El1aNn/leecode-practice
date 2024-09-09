# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        head = ListNode(-1)
        dummy = head
        tmp = 0
        while l1 or l2 or tmp:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num = val1 + val2 + tmp
            if num >= 10:
                tmp = 1
            else:
                tmp = 0
            head.next = ListNode(num % 10)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            head = head.next
        return dummy.next
