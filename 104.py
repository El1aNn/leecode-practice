# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, n):
            nonlocal ans
            if node is None:
                return n
            l = dfs(node.left, n + 1)
            r = dfs(node.right, n + 1)
            ans = max(ans, max(l, r))
            return max(l, r)

        if root is None:
            return 0

        dfs(root, 0)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print(s.maxDepth(root))
