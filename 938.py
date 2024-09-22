# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。



from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if low <= root.val <= high:
            self.res += root.val

        if root.left is not None:
            self.rangeSumBST(root.left, low, high)

        if root.right is not None:
            self.rangeSumBST(root.right, low, high)

        return self.res
