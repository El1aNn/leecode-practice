class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 反转链表

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


# 将列表转换成链表
def list_to_linked_list(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


S = Solution()
head = list_to_linked_list([1, 2, 3, 4, 5])
result = S.reverseList(head)

# 打印反转后的链表
while result:
    print(result.val, end=" ")
    result = result.next
