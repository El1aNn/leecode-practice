# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def dfs(node):
            nonlocal ans
            if not node:
                return ans
            dfs(node.left)
            ans.append(node.val)
            if self.num == k:
                return
            else:
                self.num -= 1
            dfs(node.right)
            self.num = k
        dfs(root)
        return ans[k - 1]
