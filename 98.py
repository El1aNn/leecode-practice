# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs(node, lower=float('-inf'), upper=float('inf')):
        #     if not node:
        #         return True
        #     else:
        #         if node.left.val < node.val < node.right.val:
        #             return dfs(node.left) and dfs(node.right)
        #         else:
        #             return False
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            # if not dfs(node.left, lower):

        return dfs(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False
            return True

        return dfs(root)
