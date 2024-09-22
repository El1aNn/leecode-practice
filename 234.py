# 给你一个单链表的头节点 head ，请你判断该链表是否为 回文链表。
# 如果是，返回 true ；否则，返回 false 。
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # 如果链表为空或只有一个节点，则是回文

        # 定义一个辅助函数来反转链表
        def reverseList(head: ListNode) -> ListNode:
            prev, curr = None, head
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # 使用快慢指针找到链表的中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 如果链表长度为奇数，让 slow 再移动一位
        if fast:
            slow = slow.next

        # 反转后半部分链表
        second_half = reverseList(slow)
        first_half = head

        # 比较前半部分和后半部分
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
