# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stock = []
        nums = []

        while head:
            # while stock and stock[-1][1] < head.val:
            #     ans[stock.pop()[0]] = head.val
            # stock.append([len(ans), head.val])
            # ans.append(0)
            # head = head.next
            nums.append(head.val)
            head = head.next
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            while stock and nums[stock[-1]] < nums[i]:
                ans[stock.pop()] = nums[i]
            stock.append(i)

        return ans
