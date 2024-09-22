# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
#
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
# Definition for a binary tree node.
from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        # def dfs(node: TreeNode, steel):
        #     if node is None:
        #         return 0
        #     if steel:
        #         return dfs(node.left, 0) + dfs(node.right, 0) + node.val
        #     return max(dfs(node.left, 1), dfs(node.left, 0)) + max(dfs(node.right, 0), dfs(node.right, 1))
        #
        # return max(dfs(root, 0), dfs(root, 1))
        def dfs(node):
            if not node:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            rob = l_not_rob + r_not_rob + node.val
            rob_not = max(l_not_rob, l_rob) + max(r_not_rob, r_rob)
            return rob, rob_not

        return max(dfs(root))
