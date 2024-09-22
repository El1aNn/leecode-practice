# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         self.ans = 0
#
#         def dfs(node, sum):
#             if not node: return
#             sum += node.val
#             if sum == targetSum:
#                 self.ans += 1
#             dfs(node.left, sum)
#             dfs(node.right, sum)
#
#         def search(node):
#             if not node: return
#             dfs(node, 0)
#             search(node.left)
#             search(node.right)
#
#         search(root)
#
#         return self.ans

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         self.ans = 0
#         prefix_sums = {0: 1}
#
#         def dfs(node, curr_sum):
#             if not node:
#                 return
#             curr_sum += node.val
#
#             # Check if there's a prefix sum that matches current_sum - targetSum
#             self.ans += prefix_sums.get(curr_sum - targetSum, 0)
#
#             # Update the prefix_sums dictionary
#             prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
#
#             # Continue the DFS traversal
#             dfs(node.left, curr_sum)
#             dfs(node.right, curr_sum)
#
#             # Backtrack to remove the current node's value from the prefix_sums
#             prefix_sums[curr_sum] -= 1
#
#         dfs(root, 0)
#         return self.ans
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        d = {0: 1}

        def dfs(node, sum):
            if not node: return
            sum += node.val

            self.ans += d.get(sum - targetSum, 0)

            d[sum] = d.get(sum, 0) + 1

            dfs(node.left, sum)
            dfs(node.right, sum)
            d[sum] -= 1

        return self.ans
