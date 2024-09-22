# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {element: i for i, element in enumerate(inorder)}

        def dfs(preorder: List[int], inorder: List[int]):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            pos = index[preorder[0]]
            root.left = dfs(preorder[1:pos + 1], inorder[:pos])
            root.right = dfs(preorder[pos + 1:], inorder[pos + 1:])
            return root

        return dfs(preorder, inorder)



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pos + 1], inorder[0:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])

        return root
