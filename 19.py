# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        num = 0

        def getLength(head):
            nonlocal num
            while head:
                num += 1
                head = head.next
            return num

        l = getLength(head) - n
        cur = dummy
        while l:
            cur = cur.next
            l -= 1
        cur.next = cur.next.next
        return dummy.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        双指针法：使用两个指针 left 和 right，初始时都指向哨兵节点 dummy。
        right 指针先向右移动 n 步，然后 left 和 right 一起向右移动，
        直到 right 指针到达链表的末尾。此时，left 指针指向的节点就是倒数第 n 个节点的前一个节点。
        '''
        left = right = dummy = ListNode(next = head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next # 左指针的下一个节点就是倒数第n个节点
        return dummy.next