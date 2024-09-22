# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        n = 0
        cur = head #不能直接用head，因为head可能被修改
        while cur:
            n += 1
            cur = cur.next
        if n < k:
            return dummy.next
        pre = None
        cur = head
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur # pre 最后一个节点
                cur = nxt # cur 指向下一个节点
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
            
            
            
            