# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        def getLength(node):
            ans = 0
            while node:
                node = node.next
                ans += 1
            return ans

        lengthA = getLength(headA)
        lengthB = getLength(headB)
        while lengthA < lengthB:
            headB = headB.next
            lengthB -= 1
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1
        while headB and headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
