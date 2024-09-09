# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#
#         if root is None: return ans
#
#         ans.extend(self.inorderTraversal(root.left))
#         ans.append(root.val)
#         ans.extend(self.inorderTraversal(root.right))
#
#         return ans
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         stack = []
#         if root is None: return ans
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#
#             node = stack.pop()
#             ans.append(node.val)
#             root = node.right
#
#         return ans
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# 示例用法
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorderTraversal(root))  # 输出 [1, 2, 4, 5, 3]